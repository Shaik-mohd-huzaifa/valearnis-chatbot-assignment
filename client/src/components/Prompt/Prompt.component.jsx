import "./Prompt.Styles.scss"
export const Prompt = ({text, type}) => {
    return (
        <div className={`prompt ${type}`}>
            <p>{text}</p>
            </div>
    )
}