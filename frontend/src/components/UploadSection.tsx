import { useRef, useState } from "react";
 
export default function UploadSection() {
  const [jd, setJd] = useState<File | null>(null);
  const [resumes, setResumes] = useState<File[]>([]);
  const [message, setMessage] = useState("");
  const [rankings, setRankings] = useState<any[]>([]);
  const [jdSummary, setJdSummary] = useState<any>(null);
  const [selectedCandidate, setSelectedCandidate] = useState<any>(null);
 
  const jdInputRef = useRef<HTMLInputElement>(null);
  const resumeInputRef = useRef<HTMLInputElement>(null);
 
  const handleUpload = async () => {
    if (!jd || resumes.length === 0) {
      setMessage("Please upload a JD and at least one resume.");
      return;
    }
 
    try {
      const formData = new FormData();
      formData.append("jd", jd);
 
      resumes.forEach((resume) => {
        formData.append("resumes", resume);
      });
 
      const response = await fetch("http://127.0.0.1:8000/ats/upload-bulk", {
        method: "POST",
        body: formData,
      });
 
      const data = await response.json();
 
      if (!response.ok) {
        setMessage(`Backend Error: ${JSON.stringify(data)}`);
        return;
      }
 
      setMessage(`✅ Uploaded ${data.resume_count} resumes successfully`);
    } catch (error) {
      console.error(error);
      setMessage("❌ Upload failed");
    }
  };
 
  const handleRank = async () => {
    try {
      setMessage("⏳ Ranking candidates...");
 
      const response = await fetch("http://127.0.0.1:8000/ats/bulk-rank", {
        method: "POST",
      });
 
      const data = await response.json();
      console.log("FULL RESPONSE:", data);
      console.log("CANDIDATES:", data.candidates);
 
      setRankings(data.candidates);
      setJdSummary(data.jd_summary);
 
      if (data.candidates.length > 0) {
        setSelectedCandidate(data.candidates[0]);
      }
 
      setMessage("🏆 Ranking completed successfully");
    } catch (error) {
      console.error(error);
      setMessage("❌ Ranking failed");
    }
  };
 
  const getMedal = (rank: number) => {
    if (rank === 1) return "🥇";
    if (rank === 2) return "🥈";
    if (rank === 3) return "🥉";
    return `#${rank}`;
  };
 
  return (
    <div className="space-y-8">
      {/* JD Upload */}
      <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-6 border border-white/20">
        <h2 className="text-xl font-bold text-white mb-4">
          📄 Job Description
        </h2>
 
        <input
          type="file"
          accept=".pdf,.doc,.docx,.txt"
          ref={jdInputRef}
          onChange={(e) => setJd(e.target.files?.[0] || null)}
          className="hidden"
        />
 
        <button
          onClick={() => jdInputRef.current?.click()}
          className="bg-blue-600 hover:bg-blue-700 px-5 py-3 rounded-lg text-white font-semibold"
        >
          Choose JD
        </button>
 
        <p className="text-gray-300 mt-3">
          {jd ? jd.name : "No JD selected"}
        </p>
      </div>
 
      {/* Resume Upload */}
      <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-6 border border-white/20">
        <h2 className="text-xl font-bold text-white mb-4">
          📁 Candidate Resumes
        </h2>
 
        <input
          type="file"
          multiple
          accept=".pdf,.doc,.docx"
          ref={resumeInputRef}
          onChange={(e) =>
            setResumes(e.target.files ? Array.from(e.target.files) : [])
          }
          className="hidden"
        />
 
        <button
          onClick={() => resumeInputRef.current?.click()}
          className="bg-purple-600 hover:bg-purple-700 px-5 py-3 rounded-lg text-white font-semibold"
        >
          Choose Resumes
        </button>
 
        <p className="text-gray-300 mt-3">
          {resumes.length === 0
            ? "No resumes selected"
            : `${resumes.length} resumes selected`}
        </p>
      </div>
 
      {/* Buttons */}
      <div className="flex flex-col md:flex-row gap-4">
        <button
          onClick={handleUpload}
          className="flex-1 bg-blue-600 hover:bg-blue-700 transition p-4 rounded-xl font-semibold text-white"
        >
          ☁ Upload Files
        </button>
 
        <button
          onClick={handleRank}
          className="flex-1 bg-emerald-600 hover:bg-emerald-700 transition p-4 rounded-xl font-semibold text-white"
        >
          🏆 Analyze & Rank Candidates
        </button>
      </div>
 
      {/* Message */}
      {message && (
        <div className="bg-black/30 rounded-xl p-4 text-white">
          {message}
        </div>
      )}
 
      {/* JD Analysis */}
      {jdSummary && (
        <div className="bg-white/10 backdrop-blur-lg rounded-2xl border border-white/20 p-6">
          <h2 className="text-2xl font-bold text-white mb-4">
            📄 JD Analysis
          </h2>
 
          <div className="grid md:grid-cols-2 gap-6">
            <div>
              <h3 className="text-green-400 font-bold mb-2">
                Required Skills
              </h3>
              <div className="flex flex-wrap gap-2">
                {jdSummary.required_skills?.map((skill: string, i: number) => (
                  <span
                    key={i}
                    className="bg-green-600 px-3 py-1 rounded-lg text-white"
                  >
                    {skill}
                  </span>
                ))}
              </div>
            </div>
 
            <div>
              <h3 className="text-red-400 font-bold mb-2">
                Critical Skills
              </h3>
              <div className="flex flex-wrap gap-2">
                {jdSummary.critical_skills?.map((skill: string, i: number) => (
                  <span
                    key={i}
                    className="bg-red-600 px-3 py-1 rounded-lg text-white"
                  >
                    {skill}
                  </span>
                ))}
              </div>
            </div>
          </div>
        </div>
      )}
 
      {/* Summary Stats */}
      {rankings.length > 0 && (
        <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
          <div className="bg-white/10 backdrop-blur-lg rounded-2xl border border-white/20 p-5">
            <p className="text-gray-400 text-sm">Total Candidates</p>
            <p className="text-3xl font-bold text-white mt-2">
              {rankings.length}
            </p>
          </div>
 
          <div className="bg-white/10 backdrop-blur-lg rounded-2xl border border-white/20 p-5">
            <p className="text-gray-400 text-sm">Average ATS</p>
            <p className="text-3xl font-bold text-blue-400 mt-2">
              {(
                rankings.reduce((sum, c) => sum + Number(c.ats_score || 0), 0) /
                rankings.length
              ).toFixed(1)}
            </p>
          </div>
 
          <div className="bg-white/10 backdrop-blur-lg rounded-2xl border border-white/20 p-5">
            <p className="text-gray-400 text-sm">Strong Fits</p>
            <p className="text-3xl font-bold text-green-400 mt-2">
              {rankings.filter((c) => c.fit_category === "Strong Fit").length}
            </p>
          </div>
 
          <div className="bg-white/10 backdrop-blur-lg rounded-2xl border border-white/20 p-5">
            <p className="text-gray-400 text-sm">Interview Recommended</p>
            <p className="text-3xl font-bold text-purple-400 mt-2">
              {
                rankings.filter(
                  (c) => c.hiring_recommendation === "Interview Recommended"
                ).length
              }
            </p>
          </div>
        </div>
      )}
 
      {/* ATS Split Layout */}
      {rankings.length > 0 && (
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* LEFT PANEL */}
          <div className="lg:col-span-1 bg-white/10 backdrop-blur-lg rounded-2xl border border-white/20 p-5">
            <h2 className="text-2xl font-bold text-white mb-5">🏆 Rankings</h2>
 
            <div className="space-y-3">
              {rankings.map((candidate, index) => (
                <div
                  key={index}
                  onClick={() => setSelectedCandidate(candidate)}
                  className={`cursor-pointer rounded-xl p-4 transition-all ${
                    selectedCandidate?.name === candidate.name
                      ? "bg-blue-600"
                      : "bg-white/5 hover:bg-white/10"
                  }`}
                >
                  <div className="flex justify-between items-center">
                    <div>
                      <div className="text-lg font-bold text-white">
                        {getMedal(index + 1)} {candidate.name}
                      </div>
                      <div className="text-sm text-gray-300">
                        ATS: {candidate.ats_score}
                      </div>
                    </div>
                    <div className="bg-black/30 px-3 py-2 rounded-lg text-white font-bold">
                      {Number(candidate.final_score).toFixed(2)}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
 
          {/* RIGHT PANEL */}
          <div className="lg:col-span-2 bg-white/10 backdrop-blur-lg rounded-2xl border border-white/20 p-6">
            {selectedCandidate ? (
              <>
                <h2 className="text-3xl font-bold text-white mb-6">
                  {selectedCandidate.name}
                </h2>
 
                <p className="text-yellow-400 text-lg font-semibold mb-4">
                  {selectedCandidate.rank}
                </p>
 
                <div className="flex gap-3 mb-6">
                  <span
                    className={`px-4 py-2 rounded-full text-sm font-semibold ${
                      selectedCandidate.fit_category === "Strong Fit"
                        ? "bg-green-500/20 text-green-400"
                        : selectedCandidate.fit_category === "Moderate Fit"
                        ? "bg-yellow-500/20 text-yellow-400"
                        : "bg-red-500/20 text-red-400"
                    }`}
                  >
                    {selectedCandidate.fit_category}
                  </span>
 
                  <span
                    className={`px-4 py-2 rounded-full text-sm font-semibold ${
                      selectedCandidate.hiring_recommendation ===
                      "Interview Recommended"
                        ? "bg-blue-500/20 text-blue-400"
                        : selectedCandidate.hiring_recommendation ===
                          "Needs Further Review"
                        ? "bg-yellow-500/20 text-yellow-400"
                        : "bg-gray-500/20 text-gray-400"
                    }`}
                  >
                    {selectedCandidate.hiring_recommendation}
                  </span>
                </div>
 
                {/* AI Summary */}
                <div className="bg-white/5 rounded-xl p-5 mb-6">
                  <h3 className="text-xl font-bold text-cyan-400 mb-3">
                    🤖 AI Candidate Summary
                  </h3>
                  <p className="text-gray-200 leading-relaxed">
                    {selectedCandidate.name} achieved an ATS score of{" "}
                    <span className="text-green-400 font-semibold">
                      {Number(selectedCandidate.ats_score).toFixed(2)}
                    </span>{" "}
                    and a final score of{" "}
                    <span className="text-green-400 font-semibold">
                      {Number(selectedCandidate.final_score).toFixed(2)}
                    </span>
                    . The candidate is classified as{" "}
                    <span className="text-blue-400 font-semibold">
                      {selectedCandidate.fit_category}
                    </span>{" "}
                    with a recommendation of{" "}
                    <span className="text-purple-400 font-semibold">
                      {selectedCandidate.hiring_recommendation}
                    </span>
                    . Their alignment with matched skills
                    and relevant experience are demonstrated below , the identified missing skills
                    highlight potential improvement areas.
                  </p>
                </div>
 
                {/* Resume Preview */}
                {selectedCandidate.resume_url && (
                  <div className="bg-white/5 rounded-xl p-5 mb-6">
                    <div className="flex items-center justify-between mb-4">
                      <h3 className="text-xl font-bold text-cyan-400">
                        📄 Resume Preview
                      </h3>
 
                      <a
                        href={selectedCandidate.resume_url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="bg-blue-600 hover:bg-blue-700 px-4 py-2 rounded-lg text-white text-sm"
                      >
                        Open Full Resume
                      </a>
                    </div>
 
                    <iframe
                      src={selectedCandidate.resume_url}
                      className="w-full h-[600px] rounded-lg bg-white"
                      title="Resume Preview"
                    />
                  </div>
                )}
 
                {/* Score Cards */}
                <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
                  <div className="bg-white/5 rounded-xl p-4">
                    <p className="text-gray-400">Final Score</p>
                    <p className="text-3xl font-bold text-green-400 truncate">
                      {Number(selectedCandidate.final_score).toFixed(2)}
                    </p>
                  </div>
 
                  <div className="bg-white/5 rounded-xl p-4">
                    <p className="text-gray-400">ATS Score</p>
                    <p className="text-3xl font-bold text-green-400 truncate">
                      {Number(selectedCandidate.ats_score).toFixed(2)}
                    </p>
                  </div>
 
                  <div className="bg-white/5 rounded-xl p-4">
                    <p className="text-gray-400">Skill Score</p>
                    <p className="text-3xl font-bold text-green-400 truncate">
                      {Number(selectedCandidate.skill_score ?? 0).toFixed(2)}
                    </p>
                  </div>
 
                  <div className="bg-white/5 rounded-xl p-4">
                    <p className="text-gray-400">Semantic Score</p>
                    <p className="text-3xl font-bold text-green-400 truncate">
                      {Number(selectedCandidate.semantic_score).toFixed(2)}
                    </p>
                  </div>
 
                  <div className="bg-white/5 rounded-xl p-4">
                    <p className="text-gray-400">Experience Score</p>
                    <p className="text-3xl font-bold text-green-400 truncate">
                      {Number(
                        selectedCandidate.experience_relevance_score
                      ).toFixed(2)}
                    </p>
                  </div>
 
                  <div className="bg-white/5 rounded-xl p-4">
                    <p className="text-gray-400">Keyword Score</p>
                    <p className="text-3xl font-bold text-green-400 truncate">
                      {Number(selectedCandidate.keyword_score ?? 0).toFixed(2)}
                    </p>
                  </div>
                </div>
 
                {/* Secondary Metrics */}
                <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4 mb-6">
                  <div className="bg-white/5 rounded-xl p-4">
                    <p className="text-gray-400">Project Score</p>
                    <p className="text-3xl font-bold text-green-400 truncate">
                      {Number(selectedCandidate.project_score).toFixed(2)}
                    </p>
                  </div>
 
                  <div className="bg-white/5 rounded-xl p-4">
                    <p className="text-gray-400">Education Score</p>
                    <p className="text-3xl font-bold text-green-400 truncate">
                      {Number(selectedCandidate.education_score).toFixed(2)}
                    </p>
                  </div>
 
                  <div className="bg-white/5 rounded-xl p-4">
                    <p className="text-gray-400">Certification Score</p>
                    <p className="text-3xl font-bold text-green-400 truncate">
                      {Number(selectedCandidate.certification_score).toFixed(
                        2
                      )}
                    </p>
                  </div>
                </div>
 
                {/* Strengths Weaknesses */}
                <div className="grid md:grid-cols-2 gap-6">
                  <div className="bg-white/5 rounded-xl p-5">
                    <h3 className="text-xl font-bold text-green-400 mb-3">
                      Strengths
                    </h3>
                    {selectedCandidate.strengths?.length > 0 ? (
                      <ul className="space-y-2 text-white">
                        {selectedCandidate.strengths.map(
                          (item: string, i: number) => (
                            <li key={i}>✓ {item}</li>
                          )
                        )}
                      </ul>
                    ) : (
                      <p className="text-gray-400">No strengths detected</p>
                    )}
                  </div>
 
                  <div className="bg-white/5 rounded-xl p-5">
                    <h3 className="text-xl font-bold text-red-400 mb-3">
                      Weaknesses
                    </h3>
                    {selectedCandidate.weaknesses?.length > 0 ? (
                      <ul className="space-y-2 text-white">
                        {selectedCandidate.weaknesses.map(
                          (item: string, i: number) => (
                            <li key={i}>✗ {item}</li>
                          )
                        )}
                      </ul>
                    ) : (
                      <p className="text-gray-400">No weaknesses detected</p>
                    )}
                  </div>
                </div>
 
                {/* Matched / Missing Skills */}
                <div className="grid md:grid-cols-2 gap-6 mt-6">
                  <div className="bg-white/5 rounded-xl p-5">
                    <h3 className="text-xl font-bold text-green-400 mb-3">
                      Matched Skills
                    </h3>
                    <div className="flex flex-wrap gap-2">
                      {selectedCandidate.matched_skills?.map(
                        (skill: string, i: number) => (
                          <span
                            key={i}
                            className="bg-green-600 px-3 py-1 rounded-lg text-white"
                          >
                            ✓ {skill}
                          </span>
                        )
                      )}
                    </div>
                  </div>
 
                  <div className="bg-white/5 rounded-xl p-5">
                    <h3 className="text-xl font-bold text-red-400 mb-3">
                      Missing Skills
                    </h3>
                    <div className="flex flex-wrap gap-2">
                      {selectedCandidate.missing_skills?.map(
                        (skill: string, i: number) => (
                          <span
                            key={i}
                            className="bg-red-600 px-3 py-1 rounded-lg text-white"
                          >
                            ✗ {skill}
                          </span>
                        )
                      )}
                    </div>
                  </div>
                </div>
              </>
            ) : (
              <div className="text-center text-gray-400 py-20">
                Select a candidate to view details
              </div>
            )}
          </div>
        </div>
      )}
 
      {/* Candidate Comparison Table */}
      {rankings.length > 0 && (
        <div className="bg-white/10 backdrop-blur-lg rounded-2xl border border-white/20 p-6">
          <h2 className="text-2xl font-bold text-white mb-4">
            📊 Candidate Comparison
          </h2>
 
          <table className="w-full text-white table-fixed">
            <thead>
              <tr>
                <th className="text-center p-3">Rank</th>
                <th className="text-left p-3 w-48">Name</th>
                <th className="text-right p-3">Final</th>
                <th className="text-right p-3">ATS</th>
                <th className="text-right p-3">Skill</th>
                <th className="text-right p-3">Experience</th>
                <th className="text-center p-3">Recommendation</th>
                <th className="text-center p-3">Resume</th>
              </tr>
            </thead>
 
            <tbody>
              {rankings.map((candidate: any) => (
                <tr
                  key={candidate.rank}
                  className="border-t border-white/10"
                >
                  <td className="text-center p-3">{candidate.rank}</td>
                  <td className="text-left p-3">{candidate.name}</td>
                  <td className="text-right p-3 font-mono">
                    {Number(candidate.final_score).toFixed(2)}
                  </td>
                  <td className="text-right p-3 font-mono">
                    {Number(candidate.ats_score).toFixed(2)}
                  </td>
                  <td className="text-right p-3 font-mono">
                    {Number(candidate.skill_score).toFixed(2)}
                  </td>
                  <td className="text-right p-3 font-mono">
                    {Number(candidate.experience_relevance_score).toFixed(2)}
                  </td>
                  <td className="text-center p-3">
                    <span
                      className={`px-3 py-1 rounded-full text-xs font-semibold ${
                        candidate.hiring_recommendation ===
                        "Interview Recommended"
                          ? "bg-blue-500/20 text-blue-400"
                          : candidate.hiring_recommendation ===
                            "Needs Further Review"
                          ? "bg-yellow-500/20 text-yellow-400"
                          : "bg-gray-500/20 text-gray-400"
                      }`}
                    >
                      {candidate.hiring_recommendation}
                    </span>
                  </td>
                  <td className="py-4 text-center">
                    <a
                      href={candidate.resume_url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="text-purple-400 hover:text-purple-300 underline"
                    >
                      View Resume
                    </a>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}