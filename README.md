# Property Management Backend

Django + Django REST Framework backend for a personal Pakistani property
management app. This repository is a **scaffold + schema only** — models,
admin, and stub API endpoints for every module in the spec are in place,
but business logic (auto-generating monthly rent invoices, sending
reminders, PDF reports, multi-user auth) is intentionally deferred.

A future Android client will consume the REST API exposed at `/api/v1/`.

## Modules

| App              | Purpose                                                       |
|------------------|---------------------------------------------------------------|
| `properties`     | Property records, photo gallery, scanned documents.           |
| `tenants`        | Tenant profile, CNIC, documents.                              |
| `leases`         | Lease agreements, monthly rent, annual escalation.            |
| `payments`       | Rent invoices, payments received, withholding tax tracking.   |
| `expenses`       | Expense logging with category + photos/receipts.              |
| `communications` | Tenant complaint/request log with attachments.                |
| `vault`          | FBR notices, Section 7E, NADRA, etc.                          |
| `taxes`          | Pakistani Jul–Jun tax-year aggregation endpoint.              |
| `reminders`      | Lease expiry / rent due / tax filing reminders (data only).   |

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

cp .env.example .env             # edit DATABASE_URL if you want Postgres
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

- Admin panel: `http://localhost:8000/admin/`
- REST API root: `http://localhost:8000/api/v1/`
- Tax year summary: `GET /api/v1/tax-years/<year>/` (e.g. `2025` =
  1 Jul 2024 – 30 Jun 2025)

## Database

Defaults to local SQLite. Set `DATABASE_URL` in `.env` to point at
Postgres for production.

## What's intentionally **not** built yet

- Auth & multi-user roles (single-user MVP).
- Automatic monthly invoice generation from active leases.
- Reminder delivery (email/push) — only the data model exists.
- PDF report generation.
- Withholding-tax slab calculations / FBR slab tables.
- Android client (separate project).
