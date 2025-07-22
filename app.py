import cohere
import speech_recognition as sr
from gtts import gTTS
import os

# 1. إعداد Cohere
co = cohere.Client('qwHiYwd1G2ATaopft9b4GBSDepWGexUmYm9B6Mz2')  # ← اكتبي مفتاح Cohere هنا

# 2. تحويل الصوت إلى نص
def voice_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 تكلمي الآن...")
        audio = r.listen(source)
        print("✅ تم تسجيل الصوت، جاري التحويل...")
        try:
            text = r.recognize_google(audio, language="ar-SA")  # اللغة: عربية سعودية
            print("📝 النص:", text)
            return text
        except Exception as e:
            print("❌ حصل خطأ:", e)
            return ""

# 3. توليد رد باستخدام Cohere
def get_response_from_cohere(text_input):
    response = co.chat(message=text_input)
    reply = response.text
    print("🤖 رد Cohere:", reply)
    return reply

# 4. تحويل النص إلى صوت
def text_to_voice(text):
    tts = gTTS(text=text, lang='ar')
    tts.save("reply.mp3")
    os.system("start reply.mp3")  # لو ما اشتغل الصوت قولي لي نشوف الطريقة حسب جهازك

# 5. دمج الخطوات كلها
def main():
    user_text = voice_to_text()
    if user_text:
        reply = get_response_from_cohere(user_text)
        text_to_voice(reply)

# ✅ تشغيل البرنامج بشكل صحيح
if __name__== "__main__":
    main()