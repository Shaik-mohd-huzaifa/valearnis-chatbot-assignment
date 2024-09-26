import { useState, useRef, useEffect } from "react";

const AutoResizeTextarea = () => {
  const [height, setHeight] = useState("50px");
  const textareaRef = useRef(null);

  const adjustHeight = () => {
    const textarea = textareaRef.current;
    textarea.style.height = "50px"; // Reset height to the initial height
    const scrollHeight = textarea.scrollHeight;
    const newHeight = Math.min(scrollHeight, 200); // Max height is 200px
    setHeight(`${newHeight}px`);
  };

  useEffect(() => {
    adjustHeight(); // Ensure it adjusts height initially
  }, []);

  return (
    <textarea
      ref={textareaRef}
      style={{
        width: "300px", // Fixed width
        height: height, // Dynamic height based on content
        maxHeight: "200px", // Max height
        resize: "none", // Disable resizing
        overflowY: "scroll", // Hide scrollbar when max height is reached
      }}
      onInput={adjustHeight} // Call adjustHeight on every input
      placeholder="Start typing..."
    />
  );
};

export default AutoResizeTextarea;
