from ..extensions import db

class Department(db.Model):
    __tablename__ = 'departments'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    hod_id = db.Column(db.Integer, db.ForeignKey('user.id', name='fk_department_hod', ondelete='SET NULL'), nullable=True)
    
    # Relationships
    users = db.relationship('User', back_populates='department', foreign_keys='User.department_id')
    hod = db.relationship('User', foreign_keys=[hod_id], back_populates='department_led', post_update=True)
    
    def __repr__(self):
        return f'<Department {self.name}>'
