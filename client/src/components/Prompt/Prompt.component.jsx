import "./Prompt.Styles.scss"
export const Prompt = ({text, type}) => {
    return (
        <div className={`prompt ${type}`}>
            {/* {type == "Right-Prompt" && <p className="tag">V</p>} */}
            <p>{text}</p>
            {/* {type == "left-Prompt" && <p className="tag">U</p>} */}
            </div>
    )
}