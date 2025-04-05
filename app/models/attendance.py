from datetime import datetime
from ..extensions import db

class Attendance(db.Model):
    __tablename__ = 'attendance'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), nullable=False)  # Present, Absent, Late, etc.
    recorded_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    student = db.relationship('User', 
                            foreign_keys=[student_id], 
                            backref=db.backref('attendances', lazy='dynamic'),
                            primaryjoin='Attendance.student_id == User.id')
    recorder = db.relationship('User', 
                             foreign_keys=[recorded_by], 
                             backref=db.backref('recorded_attendances', lazy='dynamic'),
                             primaryjoin='Attendance.recorded_by == User.id')

    def __repr__(self):
        return f'<Attendance {self.student_id} {self.date} {self.status}>'
