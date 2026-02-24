# Deployment Guide

## Deploy to Render

### Prerequisites
- GitHub account
- Render account (free tier available at https://render.com)

### Important Note About Ollama
⚠️ **Render Limitation**: Render's free tier doesn't support running Ollama locally. You have two options:

#### Option 1: Use Cloud-Based LLM (Recommended for Render)
Replace Ollama with a cloud-based API like:
- OpenAI API
- Anthropic Claude API
- Google Gemini API
- Groq API (free tier available)

#### Option 2: Deploy Ollama Separately
- Deploy Ollama on a separate server with GPU support
- Update the `base_url` in config.py to point to your Ollama server

### Step-by-Step Deployment

#### 1. Push to GitHub

```bash
# Add all files
git add .

# Commit changes
git commit -m "Initial commit - HealthGPT application"

# Create a new repository on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

#### 2. Deploy on Render

1. Go to https://render.com and sign in
2. Click "New +" and select "Web Service"
3. Connect your GitHub repository
4. Configure the service:
   - **Name**: healthgpt (or your preferred name)
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0 --server.headless=true`
   - **Instance Type**: Free

5. Add Environment Variables (if using cloud LLM):
   - Click "Environment" tab
   - Add your API keys (e.g., `OPENAI_API_KEY`)

6. Click "Create Web Service"

#### 3. Wait for Deployment
- Render will build and deploy your application
- This may take 5-10 minutes
- You'll get a URL like: `https://healthgpt.onrender.com`

### Alternative: Deploy to Streamlit Cloud

Streamlit Cloud is another free option that works well with Streamlit apps:

1. Go to https://streamlit.io/cloud
2. Sign in with GitHub
3. Click "New app"
4. Select your repository
5. Set main file path: `app.py`
6. Click "Deploy"

### Post-Deployment

1. Test all features
2. Check that the UI loads correctly
3. Verify chat functionality
4. Test patient profile updates

### Troubleshooting

**Issue**: App crashes on startup
- **Solution**: Check Render logs for errors
- Verify all dependencies in requirements.txt
- Ensure Python version compatibility

**Issue**: Ollama connection fails
- **Solution**: Update to use cloud-based LLM API
- Or deploy Ollama on a separate server

**Issue**: Slow response times
- **Solution**: Upgrade to paid Render tier
- Or use faster LLM API

**Issue**: Logo not displaying
- **Solution**: Ensure logo.png is committed to repository
- Check file path in app.py

### Environment Variables for Cloud LLM

If switching to OpenAI (example):

```python
# In config.py, update MODEL_CONFIG:
import os

MODEL_CONFIG = {
    "name": "gpt-3.5-turbo",
    "api_key": os.getenv("OPENAI_API_KEY"),
    "provider": "openai"
}
```

### Cost Considerations

- **Render Free Tier**: 
  - 750 hours/month
  - Spins down after 15 minutes of inactivity
  - Cold starts take 30-60 seconds

- **Streamlit Cloud Free Tier**:
  - Unlimited hours
  - 1 GB RAM
  - 1 CPU core

### Security Checklist

- [ ] Add .env to .gitignore
- [ ] Never commit API keys
- [ ] Use environment variables for secrets
- [ ] Enable HTTPS (automatic on Render)
- [ ] Review CORS settings
- [ ] Add rate limiting if needed

### Monitoring

- Check Render dashboard for:
  - CPU usage
  - Memory usage
  - Request logs
  - Error logs

### Updating Your Deployment

```bash
# Make changes to your code
git add .
git commit -m "Description of changes"
git push origin main
```

Render will automatically redeploy when you push to main branch.

### Custom Domain (Optional)

1. Go to Render dashboard
2. Select your service
3. Click "Settings"
4. Scroll to "Custom Domain"
5. Add your domain
6. Update DNS records as instructed

---

## Quick Commands Reference

```bash
# Initialize git (if not already done)
git init

# Check status
git status

# Add all files
git add .

# Commit
git commit -m "Your message"

# Add remote
git remote add origin YOUR_REPO_URL

# Push to GitHub
git push -u origin main

# Pull latest changes
git pull origin main
```

---

For more help, visit:
- Render Docs: https://render.com/docs
- Streamlit Docs: https://docs.streamlit.io/
- GitHub Docs: https://docs.github.com/
