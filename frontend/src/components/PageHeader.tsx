import { ReactNode } from "react";

export default function PageHeader({
  title,
  action,
}: {
  title: string;
  action?: ReactNode;
}) {
  return (
    <div className="flex items-center justify-between mb-4">
      <h2 className="text-xl md:text-2xl font-semibold">{title}</h2>
      {action}
    </div>
  );
}
