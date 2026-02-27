# 📸 CodeShot

A Django-based web application that converts code snippets into beautiful, shareable images with syntax highlighting, themes, and customizable styling options.

## ✨ Features

 🎨 **Syntax Highlighting**: Support for multiple programming languages
- 🌈 **Theme Support**: Various color themes for code display
- 🎯 **Customizable Styling**:
  - 🔢 Line numbers toggle
  - 🪟 Mac-style window buttons
  - 🌅 Background gradients
  - 📏 Custom padding
  - 💧 Watermark support
- 🔤 **Font Selection**: Choose from available fonts
- ⚡ **Easy to Use**: Simple web interface for generating code images

## 🛠️ Technologies Used

- 🔧 **Backend**: Django 6.0
- 🐍 **Language**: Python
- 🖼️ **Image Processing**: Pillow
- ✨ **Syntax Highlighting**: Pygments
- 🎨 **Frontend**: HTML/CSS

## 🚀 Installation

### 📋 Prerequisites

- 🐍 Python 3.8 or higher
- 📦 pip (Python package manager)

### ⚙️ Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/UmangRaj22/shareable-code-snippets.git
   cd code_shot
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   Open your browser and navigate to `http://localhost:8000` 🌐


## 💡 Usage

1. 🌐 Open the application in your browser
2. 📋 Paste your code into the text area
3. 🔤 Select your programming language
4. 🎨 Choose a theme and styling options:
   - 🌈 **Theme**: Select color scheme
   - 🔢 **Line Numbers**: Toggle line numbers
   - 🪟 **Mac Buttons**: Add macOS-style window controls
   - 🌅 **Background Gradient**: Enable gradient background
   - 📏 **Padding**: Adjust spacing around code
   - 💧 **Watermark**: Add custom text watermark
5. ✨ Click generate to create the image
6. 📥 Download or share the generated image

## 📦 Dependencies

- 🔧 **Django** (>=6.0): Web framework
- 🖼️ **Pillow** (>=10.0.0): Image processing
- ✨ **Pygments** (>=2.15.0): Syntax highlighting

## ⚙️ Configuration

### 🔧 Django Settings

Key settings are configured in `code_shot/settings.py`:
- 🐛 `DEBUG`: Set to `False` for production
- 🔐 `ALLOWED_HOSTS`: Add your domain for production
- 📱 `INSTALLED_APPS`: List of installed applications
- 💾 `STATIC_ROOT` and `MEDIA_ROOT`: File storage locations

### 🔑 Environment Variables

For production deployments, consider using environment variables for sensitive settings:
- 🔐 `SECRET_KEY`: Django secret key
- 🐛 `DEBUG`: Debug mode flag
- 🔗 `ALLOWED_HOSTS`: Allowed hostnames

## 👨‍💻 Development

### 🧪 Running Tests

```bash
python manage.py test
```

### 👤 Creating a Superuser

```bash
python manage.py createsuperuser
```

### 🔐 Access Django Admin

Navigate to `http://localhost:8000/admin` and log in with your superuser credentials.

## 🚀 Production Deployment

Before deploying to production:

1. 🐛 Set `DEBUG = False` in settings.py
2. 🔗 Update `ALLOWED_HOSTS` with your domain
3. 🔐 Generate a secure `SECRET_KEY`
4. 💾 Configure a production database (PostgreSQL recommended)
5. 🖼️ Set up static files serving (Whitenoise or CDN)
6. 🔒 Enable HTTPS
7. ⚙️ Consider using Gunicorn as WSGI server
8. 🔄 Use a reverse proxy like Nginx

## 📜 License

This project is open source and available under the MIT License.


## 💬 Support

For issues, questions, or suggestions, please open an issue on the GitHub repository.

---

