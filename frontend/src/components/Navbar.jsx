import { motion } from "framer-motion";

function Navbar() {
  return (
    <motion.nav
      className="navbar"
      initial={{
        opacity: 0,
        y: -15,
      }}
      animate={{
        opacity: 1,
        y: 0,
      }}
    >
      <div>

        <h1 className="logo">
          CreatorIQ AI
        </h1>

        <p className="subtitle">
          AI-Powered Video Intelligence Platform
        </p>

      </div>

      <div className="status-pill">
        System Ready
      </div>

    </motion.nav>
  );
}

export default Navbar;