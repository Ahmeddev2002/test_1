import { FormEvent, useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { api, Paginated } from "../api/client";
import { Tenant } from "../api/types";
import PageHeader from "../components/PageHeader";

export default function Tenants() {
  const [list, setList] = useState<Tenant[]>([]);
  const [showForm, setShowForm] = useState(false);

  const load = () =>
    api
      .get<Paginated<Tenant>>("/tenants/")
      .then((r) => setList(r.results))
      .catch(console.error);

  useEffect(() => {
    load();
  }, []);

  return (
    <>
      <PageHeader
        title="Tenants"
        action={
          <button className="btn-primary" onClick={() => setShowForm((s) => !s)}>
            {showForm ? "Cancel" : "+ Add"}
          </button>
        }
      />
      {showForm && (
        <NewTenantForm
          onSaved={() => {
            setShowForm(false);
            load();
          }}
        />
      )}
      <div className="grid gap-3 mt-4">
        {list.map((t) => (
          <Link key={t.id} to={`/tenants/${t.id}`} className="card p-4 hover:shadow-md">
            <div className="font-semibold">{t.name}</div>
            <div className="text-sm text-slate-500">
              {t.cnic} · {t.phone}
            </div>
          </Link>
        ))}
        {list.length === 0 && (
          <div className="text-slate-500 text-sm text-center py-12">No tenants yet.</div>
        )}
      </div>
    </>
  );
}

function NewTenantForm({ onSaved }: { onSaved: () => void }) {
  const [saving, setSaving] = useState(false);
  const [err, setErr] = useState<string>();

  const submit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const fd = new FormData(e.currentTarget);
    try {
      setSaving(true);
      await api.post("/tenants/", {
        name: fd.get("name"),
        cnic: fd.get("cnic"),
        phone: fd.get("phone"),
        emergency_contact_name: fd.get("emergency_contact_name") || "",
        emergency_contact_phone: fd.get("emergency_contact_phone") || "",
      });
      onSaved();
    } catch (e) {
      setErr(String(e));
    } finally {
      setSaving(false);
    }
  };

  return (
    <form onSubmit={submit} className="card p-4 space-y-3">
      <div className="grid md:grid-cols-2 gap-3">
        <div>
          <label className="label">Name</label>
          <input name="name" required className="input" />
        </div>
        <div>
          <label className="label">CNIC (XXXXX-XXXXXXX-X)</label>
          <input
            name="cnic"
            required
            pattern="\d{5}-\d{7}-\d"
            className="input"
            placeholder="35202-1234567-1"
          />
        </div>
        <div>
          <label className="label">Phone</label>
          <input name="phone" required type="tel" className="input" placeholder="03xx-xxxxxxx" />
        </div>
        <div>
          <label className="label">Emergency contact name</label>
          <input name="emergency_contact_name" className="input" />
        </div>
        <div>
          <label className="label">Emergency contact phone</label>
          <input name="emergency_contact_phone" type="tel" className="input" />
        </div>
      </div>
      {err && <div className="text-sm text-red-600">{err}</div>}
      <button className="btn-primary" disabled={saving}>
        {saving ? "Saving…" : "Save tenant"}
      </button>
    </form>
  );
}
