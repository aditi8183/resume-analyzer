import { BrowserRouter, Routes, Route } from "react-router-dom";
import ProtectedRoute from "./components/ProtectedRoute";
import Home from "./pages/Home";
import RoleSelection from "./pages/RoleSelection";
import Login from "./pages/Login";
import Register from "./pages/Register";
import CandidateDashboard from "./pages/CandidateDashboard";
import RecruiterDashboard from "./pages/RecruiterDashboard";
import ResultPage from "./pages/ResultPage";
function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/choose-role" element={<RoleSelection />}/>

        <Route path="/login" element={<Login />} />

        <Route path="/register" element={<Register />} />
         <Route
          path="/result"
          element={<ResultPage />}
        />
        <Route

          path="/recruiter"
          element={
            <ProtectedRoute>
            <RecruiterDashboard />
            </ProtectedRoute>
        
          }
        />
        <Route
          path="/candidate"
          element={
            <ProtectedRoute>
            <CandidateDashboard />
            </ProtectedRoute>
          }
        />
      </Routes>
    </BrowserRouter>
  );
}

export default App;