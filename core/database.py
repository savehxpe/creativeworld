"""
SQLite database layer for Outworld Lead Engine.
"""
import sqlite3
import os
from datetime import datetime, timedelta
from config.settings import DB_PATH


class LeadDatabase:
    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self._init_tables()

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def _init_tables(self):
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS leads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                handle TEXT UNIQUE NOT NULL,
                niche TEXT,
                website_found TEXT,
                has_website INTEGER DEFAULT 0,
                audit_pdf_path TEXT,
                outreach_dir TEXT,
                status TEXT DEFAULT 'discovered',
                contact_date TEXT,
                follow_up_1_date TEXT,
                follow_up_2_date TEXT,
                notes TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS audits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                lead_id INTEGER,
                lighthouse_scores TEXT,
                ai_summary TEXT,
                flags TEXT,
                pdf_path TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (lead_id) REFERENCES leads(id)
            )
        """)

        conn.commit()
        conn.close()

    def add_lead(self, handle, niche, website_found, has_website, audit_pdf_path=None, outreach_dir=None):
        conn = self._connect()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO leads (handle, niche, website_found, has_website, audit_pdf_path, outreach_dir)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (handle, niche, website_found, int(has_website), audit_pdf_path, outreach_dir))
            conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            # Lead already exists
            cursor.execute("SELECT id FROM leads WHERE handle = ?", (handle,))
            return cursor.fetchone()[0]
        finally:
            conn.close()

    def update_lead_status(self, handle, status, notes=None):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("UPDATE leads SET status = ?, notes = ? WHERE handle = ?", (status, notes, handle))
        conn.commit()
        conn.close()

    def schedule_follow_ups(self, handle):
        """Set follow-up dates: Day 3 and Day 7 from today."""
        contact = datetime.now().strftime("%Y-%m-%d")
        follow_1 = (datetime.now() + timedelta(days=3)).strftime("%Y-%m-%d")
        follow_2 = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")

        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE leads SET contact_date = ?, follow_up_1_date = ?, follow_up_2_date = ? WHERE handle = ?",
            (contact, follow_1, follow_2, handle)
        )
        conn.commit()
        conn.close()

    def get_pending_follow_ups(self):
        """Get leads where follow-up date is today or past."""
        today = datetime.now().strftime("%Y-%m-%d")
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT handle, niche, status, follow_up_1_date, follow_up_2_date
            FROM leads
            WHERE status IN ('contacted', 'responded')
            AND (follow_up_1_date <= ? OR follow_up_2_date <= ?)
        """, (today, today))
        rows = cursor.fetchall()
        conn.close()
        return rows

    def get_lead(self, handle):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM leads WHERE handle = ?", (handle,))
        row = cursor.fetchone()
        conn.close()
        return row

    def list_leads(self, status=None):
        conn = self._connect()
        cursor = conn.cursor()
        if status:
            cursor.execute("SELECT * FROM leads WHERE status = ? ORDER BY created_at DESC", (status,))
        else:
            cursor.execute("SELECT * FROM leads ORDER BY created_at DESC")
        rows = cursor.fetchall()
        conn.close()
        return rows
