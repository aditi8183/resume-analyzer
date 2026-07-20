import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

export default function CandidateDashboard() {
  const [jobs, setJobs] = useState<any[]>([]);
  const [selectedJob, setSelectedJob] = useState<any>(null);
  const [candidateName, setCandidateName] = useState("");
  const [resumeFile, setResumeFile] = useState<File | null>(null);

  const navigate = useNavigate();

  useEffect(() => {
    fetch("http://127.0.0.1:8000/jobs/")
      .then((res) => res.json())
      .then((data) => setJobs(data))
      .catch((err) => console.error(err));
  }, []);

  const submitApplication = async () => {
    if (!resumeFile || !candidateName) {
      alert("Please fill all fields");
      return;
    }

    try {
      const formData = new FormData();

      formData.append("name", candidateName);
      formData.append("job_id", String(selectedJob.id));
      formData.append("resume", resumeFile);

      const response = await fetch(
        "http://127.0.0.1:8000/candidate/apply",
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();

      if (!response.ok) {
        alert(data.detail || "Application failed");
        return;
      }

      localStorage.setItem(
        "applicationResult",
        JSON.stringify(data)
      );

      navigate("/result");
    } catch (error) {
      console.error(error);
      alert("Something went wrong");
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-indigo-900 to-slate-950 p-8">

      <div className="max-w-6xl mx-auto">

        <div className="mb-10 text-center">

          <h1 className="text-5xl font-bold text-white mb-3">
            Candidate Dashboard
          </h1>

          <p className="text-gray-300 text-lg">
            Browse available opportunities and apply instantly
          </p>

        </div>

        {jobs.map((job: any) => (
          <div
            key={job.id}
            className="bg-white/10 backdrop-blur-lg rounded-2xl border border-white/20 p-6 mb-6 hover:scale-[1.01] transition-all shadow-2xl"
          >

            <div className="flex justify-between items-start mb-5">

              <div>
                <h2 className="text-3xl font-bold text-white">
                  {job.title}
                </h2>

                <p className="text-gray-300 mt-2">
                  Experience Required:
                  <span className="text-white font-semibold ml-2">
                    {job.experience_required || "Not specified"}
                  </span>
                </p>
              </div>

            </div>

            <div className="mb-6">

              <h3 className="text-lg font-semibold text-purple-300 mb-3">
                Required Skills
              </h3>

              <div className="flex flex-wrap gap-2">

                {job.required_skills
                  ?.split(",")
                  .map((skill: string) => (
                    <span
                      key={skill}
                      className="bg-violet-600/30 border border-violet-400 px-3 py-2 rounded-lg text-white font-semibold"
                    >
                      {skill.trim()}
                    </span>
                  ))}

              </div>

            </div>

            {selectedJob?.id !== job.id ? (
              <button
                onClick={() => setSelectedJob(job)}
                className="bg-purple-600 hover:bg-purple-700 px-6 py-3 rounded-xl text-white font-semibold"
              >
                Apply Now
              </button>
            ) : (
              <div className="bg-black/30 rounded-2xl p-5 border border-white/10">

                <h3 className="text-xl font-bold text-white mb-4">
                  Application Form
                </h3>

                <div className="grid md:grid-cols-3 gap-4 items-center">

                  <input
                    type="text"
                    placeholder="Enter Full Name"
                    value={candidateName}
                    onChange={(e) =>
                      setCandidateName(e.target.value)
                    }
                    className="px-4 py-3 rounded-xl bg-white text-black outline-none"
                  />

                  <div>

                    <label className="w-full bg-blue-600 hover:bg-blue-700 px-5 py-3 rounded-xl text-white font-semibold text-center cursor-pointer block">

                      Choose Resume

                      <input
                        type="file"
                        hidden
                        onChange={(e) =>
                          setResumeFile(
                            e.target.files?.[0] || null
                          )
                        }
                      />

                    </label>

                    {resumeFile && (
                      <p className="text-green-300 text-sm mt-2">
                        📄 {resumeFile.name}
                      </p>
                    )}

                  </div>

                  <button
                    onClick={submitApplication}
                    className="bg-emerald-600 hover:bg-emerald-700 px-5 py-3 rounded-xl text-white font-semibold"
                  >
                    Submit Application
                  </button>

                </div>

              </div>
            )}

          </div>
        ))}

      </div>

    </div>
  );
}

