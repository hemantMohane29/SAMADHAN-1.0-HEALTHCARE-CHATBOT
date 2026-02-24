# Quick Render Deployment Steps

## ✅ GitHub Push - COMPLETED

Your code is now on GitHub at:
**https://github.com/hemantMohane29/SAMADHAN-1.0-HEALTHCARE-CHATBOT**

---

## 🚀 Next Steps: Deploy to Render

### Step 1: Sign Up/Login to Render
1. Go to https://render.com
2. Sign up or login (you can use your GitHub account)

### Step 2: Create New Web Service
1. Click the **"New +"** button in the top right
2. Select **"Web Service"**

### Step 3: Connect GitHub Repository
1. Click **"Connect account"** to link your GitHub
2. Search for: **SAMADHAN-1.0-HEALTHCARE-CHATBOT**
3. Click **"Connect"** next to your repository

### Step 4: Configure Service Settings

Fill in these details:

- **Name**: `healthgpt` (or any name you prefer)
- **Region**: Choose closest to you
- **Branch**: `master`
- **Root Directory**: (leave blank)
- **Runtime**: `Python 3`
- **Build Command**: 
  ```
  pip install -r requirements.txt
  ```
- **Start Command**: 
  ```
  streamlit run app.py --server.port=$PORT --server.address=0.0.0.0 --server.headless=true
  ```

### Step 5: Choose Plan
- Select **"Free"** plan (perfect for testing)
- Note: Free tier spins down after 15 minutes of inactivity

### Step 6: Advanced Settings (Important!)

Click **"Advanced"** and add environment variables:

⚠️ **CRITICAL**: Since Render doesn't support local Ollama, you need to either:

**Option A: Use a Cloud LLM API (Recommended)**
- Add environment variable: `OPENAI_API_KEY` = your-api-key
- Or use Groq (free): `GROQ_API_KEY` = your-api-key
- You'll need to modify `app.py` to use the cloud API instead of Ollama

**Option B: Deploy Ollama Separately**
- Deploy Ollama on a GPU server
- Add environment variable: `OLLAMA_BASE_URL` = your-ollama-server-url

### Step 7: Deploy
1. Click **"Create Web Service"**
2. Wait 5-10 minutes for deployment
3. You'll get a URL like: `https://healthgpt.onrender.com`

---

## 🔧 Required Code Changes for Cloud Deployment

Since Render doesn't support local Ollama, you need to modify the code:

### Option 1: Use OpenAI (Easiest)

1. Install OpenAI package:
   ```bash
   pip install openai langchain-openai
   ```

2. Update `requirements.txt`:
   ```
   streamlit==1.52.2
   langchain-openai==0.1.0
   openai==1.12.0
   ```

3. Modify `app.py` - replace this line:
   ```python
   from langchain_ollama import ChatOllama
   model = ChatOllama(model="gpt-oss:120b-cloud", base_url="http://localhost:11434/")
   ```
   
   With:
   ```python
   from langchain_openai import ChatOpenAI
   import os
   model = ChatOpenAI(
       model="gpt-3.5-turbo",
       api_key=os.getenv("OPENAI_API_KEY")
   )
   ```

4. Add to Render environment variables:
   - `OPENAI_API_KEY` = your-openai-api-key

### Option 2: Use Groq (Free Alternative)

1. Sign up at https://console.groq.com
2. Get free API key
3. Update code similar to OpenAI but use Groq endpoint

---

## 📝 Post-Deployment Checklist

After deployment:
- [ ] Visit your Render URL
- [ ] Test the chat interface
- [ ] Verify patient profile updates work
- [ ] Check that logo displays correctly
- [ ] Test on mobile device
- [ ] Monitor Render logs for errors

---

## 🐛 Troubleshooting

### App Won't Start
- Check Render logs (click "Logs" tab)
- Verify all dependencies in requirements.txt
- Check Python version compatibility

### Ollama Connection Error
- You MUST switch to cloud-based LLM for Render
- Local Ollama won't work on Render free tier

### Slow Performance
- Free tier has limited resources
- Consider upgrading to paid tier
- Or use faster LLM API

### Logo Not Showing
- Ensure logo.png is in repository
- Check file path in app.py
- Verify file was pushed to GitHub

---

## 💰 Cost Information

### Render Free Tier
- ✅ 750 hours/month free
- ✅ Automatic HTTPS
- ⚠️ Spins down after 15 min inactivity
- ⚠️ Cold start: 30-60 seconds

### LLM API Costs
- **OpenAI**: ~$0.002 per 1K tokens (pay as you go)
- **Groq**: Free tier available
- **Anthropic Claude**: Similar to OpenAI pricing

---

## 🔗 Useful Links

- Your GitHub Repo: https://github.com/hemantMohane29/SAMADHAN-1.0-HEALTHCARE-CHATBOT
- Render Dashboard: https://dashboard.render.com
- Render Docs: https://render.com/docs
- OpenAI API: https://platform.openai.com
- Groq Console: https://console.groq.com

---

## 📞 Need Help?

If you encounter issues:
1. Check Render logs first
2. Review DEPLOYMENT.md for detailed troubleshooting
3. Check GitHub Issues
4. Contact Render support

---

## 🎉 Success!

Once deployed, share your app URL:
`https://your-app-name.onrender.com`

Remember to add the medical disclaimer on your GitHub README!
