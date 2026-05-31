import { NavLink, Outlet } from "react-router-dom";

const nav = [
  { to: "/", label: "Dashboard", icon: "📊", end: true },
  { to: "/properties", label: "Properties", icon: "🏠" },
  { to: "/tenants", label: "Tenants", icon: "👥" },
  { to: "/leases", label: "Leases", icon: "📝" },
  { to: "/rent", label: "Rent", icon: "💰" },
  { to: "/expenses", label: "Expenses", icon: "🧾" },
  { to: "/taxes", label: "Taxes", icon: "🏛️" },
];

export default function Layout() {
  return (
    <div className="min-h-full md:grid md:grid-cols-[16rem_1fr]">
      {/* Desktop sidebar */}
      <aside className="hidden md:flex md:flex-col bg-slate-900 text-slate-100">
        <div className="p-4 text-xl font-semibold border-b border-slate-800">Property Manager</div>
        <nav className="p-2 flex-1 space-y-1">
          {nav.map((item) => (
            <NavLink
              key={item.to}
              to={item.to}
              end={item.end}
              className={({ isActive }) =>
                `flex items-center gap-2 rounded px-3 py-2 text-sm ${
                  isActive ? "bg-brand-600 text-white" : "hover:bg-slate-800"
                }`
              }
            >
              <span>{item.icon}</span>
              <span>{item.label}</span>
            </NavLink>
          ))}
        </nav>
      </aside>

      <main className="pb-20 md:pb-0">
        {/* Mobile top bar */}
        <header className="md:hidden bg-slate-900 text-white px-4 py-3 sticky top-0 z-10">
          <h1 className="text-lg font-semibold">Property Manager</h1>
        </header>

        <div className="p-4 md:p-6 max-w-5xl mx-auto">
          <Outlet />
        </div>

        {/* Mobile bottom nav */}
        <nav
          className="md:hidden fixed bottom-0 inset-x-0 bg-white border-t border-slate-200 flex justify-around z-10"
          style={{ paddingBottom: "env(safe-area-inset-bottom)" }}
        >
          {nav.slice(0, 5).map((item) => (
            <NavLink
              key={item.to}
              to={item.to}
              end={item.end}
              className={({ isActive }) =>
                `flex-1 flex flex-col items-center py-2 text-xs ${
                  isActive ? "text-brand-600" : "text-slate-500"
                }`
              }
            >
              <span className="text-lg leading-none">{item.icon}</span>
              <span className="mt-0.5">{item.label}</span>
            </NavLink>
          ))}
        </nav>
      </main>
    </div>
  );
}
