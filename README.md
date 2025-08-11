# 🌍 AI Travel Itinerary Generator

A Django web application that generates personalized travel itineraries using Azure OpenAI. Plan your perfect trip with AI-powered recommendations tailored to your preferences, budget, and travel style.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Django](https://img.shields.io/badge/Django-4.2-green.svg)
![Azure OpenAI](https://img.shields.io/badge/Azure-OpenAI-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- 🤖 **AI-Powered Planning**: Leverages Azure OpenAI to create detailed, personalized itineraries
- 🎯 **Customizable Preferences**: Choose your travel style, budget, and duration
- 📱 **Responsive Design**: Beautiful, mobile-friendly interface built with Bootstrap
- 💾 **Save & Manage**: Store your itineraries and access them anytime
- 🖨️ **Print Ready**: Export itineraries for offline use
- 🔐 **User Authentication**: Personal itinerary management (optional)
- ⚡ **Fast & Reliable**: Built with Django for scalability and performance

## 🚀 Demo

### Travel Styles Available:
- 🏔️ **Adventure**: Hiking, extreme sports, outdoor activities
- 🏛️ **Cultural**: Museums, historical sites, local experiences
- 🏖️ **Relaxation**: Spas, beaches, peaceful destinations
- 👨‍👩‍👧‍👦 **Family-friendly**: Kid-friendly activities and attractions
- 💼 **Business**: Efficient travel with networking opportunities

### Budget Options:
- 💰 **Budget-friendly**: Economical travel options
- 🏨 **Mid-range**: Comfortable accommodations and experiences
- 💎 **Luxury**: Premium experiences and high-end accommodations

## 🛠️ Technology Stack

- **Backend**: Django 4.2, Python 3.8+
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **AI Integration**: Azure OpenAI API
- **Database**: SQLite (development), PostgreSQL/MySQL (production ready)
- **Authentication**: Django's built-in authentication system

## 📋 Prerequisites

- Python 3.8 or higher
- Azure OpenAI resource with deployed model
- pip (Python package manager)
- Git

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/ai-travel-itinerary-generator.git
cd ai-travel-itinerary-generator
```

### 2. Create Virtual Environment
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration
Create a `.env` file in the project root:
```env
# Azure OpenAI Configuration
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_API_KEY=your_azure_openai_api_key_here
AZURE_OPENAI_API_VERSION=2024-02-01
AZURE_OPENAI_DEPLOYMENT_NAME=your_deployment_name

# Django Configuration
SECRET_KEY=your-super-secret-django-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 5. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 7. Test Azure OpenAI Connection
```bash
python manage.py test_azure_openai
```

### 8. Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to start planning your trips! 🎉

## 🔧 Azure OpenAI Setup

### Getting Your Credentials:

1. **Azure OpenAI Endpoint**:
   - Navigate to your Azure OpenAI resource in the Azure portal
   - Copy the "Endpoint" URL from the resource overview

2. **API Key**:
   - Go to "Keys and Endpoint" in your Azure OpenAI resource
   - Copy either "KEY 1" or "KEY 2"

3. **Deployment Name**:
   - Navigate to "Model deployments" in your Azure OpenAI resource
   - Use the exact name of your deployed model (e.g., "gpt-35-turbo-16k")

4. **API Version**:
   - Use "2024-02-01" for the latest stable version

### Supported Models:
- GPT-3.5-turbo
- GPT-4
- GPT-4-turbo
- Any other chat completion models deployed in your Azure OpenAI resource

## 📁 Project Structure

```
ai-travel-itinerary-generator/
├── 📄 manage.py
├── 📄 requirements.txt
├── 📄 .env
├── 📄 README.md
├── 📁 travel_planner/
│   ├── ⚙️ settings.py
│   ├── 🔗 urls.py
│   └── 📄 wsgi.py
├── 📁 itinerary/
│   ├── 🎯 models.py
│   ├── 👁️ views.py
│   ├── 📝 forms.py
│   ├── 🤖 services.py
│   ├── ⚡ azure_utils.py
│   └── 🔗 urls.py
├── 📁 templates/
│   ├── 🏠 base.html
│   └── 📁 itinerary/
│       ├── 🏡 home.html
│       ├── 📋 detail.html
│       └── 📊 my_itineraries.html
└── 📁 static/ (optional)
```

## 🐛 Troubleshooting

### Common Issues:

| Issue | Solution |
|-------|----------|
| **Authentication Failed** | Verify your `AZURE_OPENAI_API_KEY` is correct and active |
| **Deployment Not Found** | Check your `AZURE_OPENAI_DEPLOYMENT_NAME` matches exactly |
| **Connection Timeout** | Verify your internet connection and `AZURE_OPENAI_ENDPOINT` URL |
| **Rate Limiting** | Wait a few moments and try again (based on your Azure pricing tier) |

### Testing Your Setup:
```bash
python manage.py test_azure_openai
```

This command will validate your configuration and test the connection to Azure OpenAI.

## 🚀 Deployment

### Production Environment Variables:
```env
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
SECRET_KEY=your-production-secret-key
```

### Deployment Platforms:
- **Azure App Service**: Native integration with Azure OpenAI
- **Heroku**: Easy deployment with Postgres addon
- **AWS Elastic Beanstalk**: Scalable deployment option
- **DigitalOcean App Platform**: Cost-effective solution

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Setup:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Areas for Contribution:
- [ ] Add more travel style options
- [ ] Implement user reviews and ratings
- [ ] Add map integration
- [ ] Create mobile app version
- [ ] Add multi-language support
- [ ] Implement itinerary sharing features

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Django](https://djangoproject.com/) for the amazing web framework
- [Azure OpenAI](https://azure.microsoft.com/en-us/products/cognitive-services/openai-service/) for powerful AI capabilities
- [Bootstrap](https://getbootstrap.com/) for the beautiful UI components
- The open-source community for inspiration and support

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting](#-troubleshooting) section
2. Run the connection test: `python manage.py test_azure_openai`
3. Create an issue on GitHub
4. Check Azure OpenAI documentation

## 🔮 Future Enhancements

- [ ] Integration with booking platforms (hotels, flights)
- [ ] Real-time weather integration
- [ ] Multi-city trip planning
- [ ] Collaborative trip planning
- [ ] Mobile app development
- [ ] Integration with calendar apps
- [ ] Expense tracking
- [ ] Photo recommendations for each destination

---

**Made with ❤️ and AI**

If you find this project useful, please consider giving it a ⭐ on GitHub!


**Ready to plan your next adventure? Let AI be your travel guide! 🧳✈️**


