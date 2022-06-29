import "./about.css";
import React, { useState } from "react";

const About = () => {
  const [visible, setVisible] = useState(false);

  const showEmail = () => {
    setVisible(true);
  };

  const hideEmail = () => {
    setVisible(false);
  };

  const getContent = () => {
    if (visible) {
      return (
        <div>
          <h6>email address</h6>
          <button onClick={hideEmail} className="btn btn-outline-secondary">
            Hide Info
          </button>
        </div>
      );
    } else {
      return (
        <div>
          <p>click the button below</p>
          <button onClick={showEmail} className="btn btn-outline-secondary">
            Show Info
          </button>
        </div>
      );
    }
  };

  return (
    <div className="about-page">
      <h4>Arthur Murphy</h4>
      {getContent()}
    </div>
  );
};

export default About;
