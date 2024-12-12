# YouTube Blog Creator Using CrewAI

A Python-based project that transforms YouTube video content into structured blogs using CrewAI and OpenAI APIs. The project leverages advanced AI models to extract insights, summarize video content, and generate well-written blog posts.

---

## Features

- **Automated Blog Creation**: Converts YouTube videos into detailed blog articles.
- **AI-Powered Insights**: Uses OpenAI's GPT models to extract meaningful information.
- **Customizable Output**: Adjust the tone, style, and length of the blogs.
- **Batch Processing**: Handles multiple videos in one run.
- **Error Handling**: Includes retry logic and logging for debugging.

---

## Prerequisites

- **Python 3.8+**
- OpenAI API Key ([Sign up here](https://platform.openai.com/signup/))
- YouTube Data API Key ([Get your API key](https://developers.google.com/youtube/registering_an_application))

---

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Lavishgangwani/Youtube-Blog-Creator-Using-CrewAI.git
   cd youtube-blog-creator
   ```

2. **Set Up a Virtual Environment:**
   ```bash
   python -m venv crew_env
   source crew_env/bin/activate   # On Windows: crew_env\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set API Keys:**
   - Create a `.env` file in the project root:
     ```env
     OPENAI_API_KEY=your_openai_api_key
     YOUTUBE_API_KEY=your_youtube_api_key
     ```

---

## Usage

1. **Run the Script:**
   ```bash
   python crew.py
   ```

2. **Inputs:**
   - Provide the topic or keywords to identify relevant YouTube videos.
   - The script fetches video metadata and generates corresponding blog posts.

3. **Output:**
   - The generated blog posts are saved as `.txt` or `.md` files in the `output/` directory.

---

## File Structure

```plaintext
youtube-blog-creator/
├── crew.py               # Main script
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── .env                  # API keys (excluded from version control)
├── output/               # Generated blog files
└── utils/                # Utility modules
```

---

## Troubleshooting

- **Rate Limit Exceeded:**
  Ensure your OpenAI plan has sufficient quota. Upgrade if necessary.

- **Missing Arguments Error:**
  Update all dependencies:
  ```bash
  pip install --upgrade crewai litellm openai
  ```

- **Verbose Logging:**
  Enable detailed logs by adding this line to your script:
  ```python
  import litellm
  litellm.set_verbose(True)
  ```

---

## Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit changes: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Create a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

- [CrewAI](https://crew.ai/) for task management and automation.
- [OpenAI](https://openai.com/) for its powerful GPT models.
- [YouTube Data API](https://developers.google.com/youtube) for video metadata.

---

## Contact

For questions or support, feel free to open an issue or reach out at lavishgangwani22@gmail.com.
