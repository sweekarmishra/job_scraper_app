class JobDatabaseRouter:
    """
    Routes job-related models to MongoDB and all other models to SQLite.
    """

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'job_scraper_app':  # Replace with your actual app name
            return 'mongodb'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'job_scraper_app':
            return 'mongodb'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return True  # Allow relations between models in both databases

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'job_scraper_app':
            return db == 'mongodb'
        return db == 'default'