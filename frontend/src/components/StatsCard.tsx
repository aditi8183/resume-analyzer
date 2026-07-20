type StatsCardProps = {
  title: string;
  value: string;
  color: string;
};

export default function StatsCard({
  title,
  value,
  color,
}: StatsCardProps) {
  return (
    <div className="bg-white/5 border border-white/10 rounded-2xl p-6">
      <p className="text-gray-400 text-sm">{title}</p>

      <h3
        className={`text-3xl font-bold mt-2 ${color}`}
      >
        {value}
      </h3>
    </div>
  );
}