from app.core.database import engine, Base
# import your Academic model (even if empty for now)
try:
    from app.models.academic_model import Academic
except ImportError:
    print("Academic model not found yet, skipping import.")

# Create all tables (currently only base tables, Academic can be empty)
Base.metadata.create_all(bind=engine)

print("Database tables created successfully!")
