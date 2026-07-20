
import { useLocation, useNavigate } from "react-router-dom";

export default function ResultPage() {
  const location = useLocation();
  const navigate = useNavigate();

  const result =
    location.state ||
    JSON.parse(
      localStorage.getItem("applicationResult") || "{}"
    );

  if (!result || Object.keys(result).length === 0) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-slate-900 via-indigo-900 to-slate-950 flex justify-center items-center">

        <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-8 text-center border border-white/20">

          <h2 className="text-white text-3xl font-bold mb-4">
            No Result Found
          </h2>

          <button
            onClick={() => navigate("/candidate")}
            className="bg-blue-600 hover:bg-blue-700 px-5 py-3 rounded-xl text-white font-semibold"
          >
            Back to Dashboard
          </button>

        </div>

      </div>
    );
  }

  const score = Math.round(result.ats_score || 0);

  const scoreColor =
    score >= 70
      ? "text-green-400"
      : score >= 40
      ? "text-yellow-400"
      : "text-red-400";

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-indigo-900 to-slate-950 p-8">

      <div className="max-w-6xl mx-auto">

        <div className="text-center mb-10">

          <h1 className="text-5xl font-bold text-white mb-3">
            ATS Analysis Report
          </h1>

          <p className="text-gray-300 text-lg">
            Resume Evaluation Completed Successfully
          </p>

        </div>

        <div className="bg-white/10 backdrop-blur-lg rounded-3xl border border-white/20 shadow-2xl p-10 mb-8 text-center">

          <h3 className="text-gray-300 text-xl mb-4">
            ATS MATCH SCORE
          </h3>

          <h1
            className={`text-8xl font-bold ${scoreColor}`}
          >
            {score}%
          </h1>

          <div className="flex justify-center gap-3 mt-6">

            <span className="bg-green-600 px-4 py-2 rounded-full text-white font-semibold">
              {result.fit_category || "N/A"}
            </span>

            <span className="bg-blue-600 px-4 py-2 rounded-full text-white font-semibold">
              {result.hiring_recommendation || "N/A"}
            </span>

          </div>

        </div>

        <div className="grid md:grid-cols-2 gap-6 mb-8">

          <div className="bg-white/10 backdrop-blur-lg rounded-2xl border border-white/20 p-6">

            <h2 className="text-2xl font-bold text-green-400 mb-4">
              ✓ Matched Skills
            </h2>

            <div className="flex flex-wrap gap-2">

              {result.matched_skills?.length ? (
                result.matched_skills.map(
                  (skill: string, idx: number) => (
                    <span
                      key={idx}
                      className="bg-green-600/30 border border-green-400 px-3 py-2 rounded-lg text-white"
                    >
                      {skill}
                    </span>
                  )
                )
              ) : (
                <p className="text-gray-300">
                  No matched skills found
                </p>
              )}

            </div>

          </div>

          <div className="bg-white/10 backdrop-blur-lg rounded-2xl border border-white/20 p-6">

            <h2 className="text-2xl font-bold text-red-400 mb-4">
              ✗ Missing Skills
            </h2>

            <div className="flex flex-wrap gap-2">

              {result.missing_skills?.length ? (
                result.missing_skills.map(
                  (skill: string, idx: number) => (
                    <span
                      key={idx}
                      className="bg-red-600/30 border border-red-400 px-3 py-2 rounded-lg text-white"
                    >
                      {skill}
                    </span>
                  )
                )
              ) : (
                <p className="text-gray-300">
                  No missing skills found
                </p>
              )}

            </div>

          </div>

        </div>

        <div className="grid md:grid-cols-2 gap-6 mb-8">

          <div className="bg-white/10 backdrop-blur-lg rounded-2xl border border-white/20 p-6">

            <h2 className="text-2xl font-bold text-green-400 mb-4">
              🚀 Strengths
            </h2>

            <ul className="space-y-2">

              {result.strengths?.length ? (
                result.strengths.map(
                  (item: string, idx: number) => (
                    <li
                      key={idx}
                      className="text-white"
                    >
                      ✓ {item}
                    </li>
                  )
                )
              ) : (
                <p className="text-gray-300">
                  No strengths available
                </p>
              )}

            </ul>

          </div>

          <div className="bg-white/10 backdrop-blur-lg rounded-2xl border border-white/20 p-6">

            <h2 className="text-2xl font-bold text-yellow-400 mb-4">
              ⚠ Areas For Improvement
            </h2>

            <ul className="space-y-2">

              {result.weaknesses?.length ? (
                result.weaknesses.map(
                  (item: string, idx: number) => (
                    <li
                      key={idx}
                      className="text-white"
                    >
                      • {item}
                    </li>
                  )
                )
              ) : (
                <p className="text-gray-300">
                  No weaknesses available
                </p>
              )}

            </ul>

          </div>

        </div>

        <div className="flex justify-center gap-4">

          <button
            onClick={() => navigate("/candidate")}
            className="bg-blue-600 hover:bg-blue-700 px-8 py-3 rounded-xl text-white font-semibold"
          >
            Apply For More Jobs
          </button>

          <button
            onClick={() => {
              localStorage.clear();
              navigate("/login");
            }}
            className="bg-red-600 hover:bg-red-700 px-8 py-3 rounded-xl text-white font-semibold"
          >
            Logout
          </button>

        </div>

      </div>

    </div>
  );
}



