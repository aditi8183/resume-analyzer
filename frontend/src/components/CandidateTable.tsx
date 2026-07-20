const candidates = [
  {
    rank: 1,
    name: "Sneha Sharma",
    score: 94,
    recommendation: "Hire",
  },
  {
    rank: 2,
    name: "Rahul Verma",
    score: 91,
    recommendation: "Hire",
  },
  {
    rank: 3,
    name: "Priya Singh",
    score: 88,
    recommendation: "Consider",
  },
  {
    rank: 4,
    name: "Amit Kumar",
    score: 72,
    recommendation: "Reject",
  },
];

export default function CandidateTable() {
  return (
    <div className="bg-white/5 border border-white/10 rounded-2xl p-6">
      <h3 className="text-xl font-bold text-white mb-5">
        Candidate Rankings
      </h3>

      <table className="w-full">
        <thead>
          <tr className="text-left text-gray-400 border-b border-white/10">
            <th className="pb-3">Rank</th>
            <th className="pb-3">Candidate</th>
            <th className="pb-3">Score</th>
            <th className="pb-3">Recommendation</th>
          </tr>
        </thead>

        <tbody>
          {candidates.map((candidate) => (
            <tr
              key={candidate.rank}
              className="border-b border-white/5"
            >
              <td className="py-4 text-white">
                #{candidate.rank}
              </td>

              <td className="py-4 text-white">
                {candidate.name}
              </td>

              <td className="py-4 text-purple-400 font-bold">
                {candidate.score}%
              </td>

              <td className="py-4">
                <span
                  className={`px-3 py-1 rounded-full text-xs ${
                    candidate.recommendation === "Hire"
                      ? "bg-green-500/20 text-green-400"
                      : candidate.recommendation ===
                        "Consider"
                      ? "bg-yellow-500/20 text-yellow-400"
                      : "bg-red-500/20 text-red-400"
                  }`}
                >
                  {candidate.recommendation}
                </span>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}