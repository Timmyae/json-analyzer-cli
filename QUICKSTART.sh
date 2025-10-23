#!/bin/bash
###############################################################################
# 🚀 JSON ANALYZER - تشغيل فوري بنقرة واحدة
# هذا الملف يقوم بكل شيء تلقائياً بدون أي تدخل منك!
###############################################################################

echo "════════════════════════════════════════════════════════════════════"
echo "  🔧 JSON Analyzer CLI - التشغيل التلقائي"
echo "════════════════════════════════════════════════════════════════════"
echo ""

# ✅ الخطوة 1: التحقق من Python
echo "🔍 جاري التحقق من وجود Python..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python غير مثبت! يرجى تثبيت Python 3.7+ أولاً"
    echo "   تحميل من: https://www.python.org/downloads/"
    exit 1
fi

PYTHON_VERSION=$(python3 --version)
echo "✅ تم العثور على: $PYTHON_VERSION"
echo ""

# ✅ الخطوة 2: إنشاء ملفات اختبار JSON تلقائياً
echo "📝 جاري إنشاء ملفات JSON للاختبار..."

# ملف اختبار بسيط
cat > test_simple.json << 'EOF'
{
  "name": "مشروع تجريبي",
  "version": "1.0.0",
  "config": {
    "debug": true,
    "port": 8080
  },
  "features": ["analysis", "validation", "pretty-print"]
}
EOF

# ملف اختبار مع تكرارات
cat > test_duplicates.json << 'EOF'
{
  "users": [
    {"id": 1, "name": "أحمد"},
    {"id": 2, "name": "فاطمة"},
    {"id": 1, "name": "أحمد"}
  ],
  "tags": ["python", "json", "cli", "python"]
}
EOF

# ملف اختبار معقد
cat > test_complex.json << 'EOF'
{
  "api": {
    "version": "2.0",
    "endpoints": [
      {"path": "/users", "method": "GET"},
      {"path": "/posts", "method": "POST"}
    ],
    "authentication": {
      "type": "JWT",
      "required": true,
      "timeout": 3600
    }
  },
  "database": {
    "host": "localhost",
    "port": 5432,
    "name": "mydb",
    "credentials": null
  },
  "features": {
    "caching": true,
    "logging": true,
    "monitoring": false
  }
}
EOF

echo "✅ تم إنشاء 3 ملفات اختبار:"
echo "   - test_simple.json (بسيط)"
echo "   - test_duplicates.json (يحتوي على تكرارات)"
echo "   - test_complex.json (معقد بمستويات متعددة)"
echo ""

# ✅ الخطوة 3: جعل الأداة قابلة للتنفيذ
echo "⚙️  جاري تجهيز الأداة..."
chmod +x json_analyzer.py 2>/dev/null || echo "   (تم تخطي chmod)"
echo "✅ الأداة جاهزة للاستخدام"
echo ""

# ✅ الخطوة 4: تشغيل أمثلة توضيحية
echo "════════════════════════════════════════════════════════════════════"
echo "  📊 تشغيل الأمثلة التوضيحية"
echo "════════════════════════════════════════════════════════════════════"
echo ""

echo "▶️  مثال 1: تحليل ملف JSON بسيط"
echo "────────────────────────────────────────────────────────────────────"
python3 json_analyzer.py test_simple.json --analyze
echo ""

echo "▶️  مثال 2: كشف التكرارات"
echo "────────────────────────────────────────────────────────────────────"
python3 json_analyzer.py test_duplicates.json --duplicates
echo ""

echo "▶️  مثال 3: التحقق من Schema"
echo "────────────────────────────────────────────────────────────────────"
python3 json_analyzer.py test_simple.json --validate "name,version,config"
echo ""

echo "▶️  مثال 4: تحليل كامل للملف المعقد"
echo "────────────────────────────────────────────────────────────────────"
python3 json_analyzer.py test_complex.json --analyze
echo ""

# ✅ الخطوة 5: عرض طرق الاستخدام
echo "════════════════════════════════════════════════════════════════════"
echo "  🎓 كيفية الاستخدام المستقبلي"
echo "════════════════════════════════════════════════════════════════════"
echo ""
echo "📌 لتحليل أي ملف JSON خاص بك:"
echo "   python3 json_analyzer.py YOUR_FILE.json --analyze"
echo ""
echo "📌 للتحقق من مفاتيح معينة:"
echo "   python3 json_analyzer.py YOUR_FILE.json --validate \"key1,key2,key3\""
echo ""
echo "📌 لطباعة JSON بشكل جميل:"
echo "   python3 json_analyzer.py YOUR_FILE.json --pretty"
echo ""
echo "📌 للبحث عن التكرارات:"
echo "   python3 json_analyzer.py YOUR_FILE.json --duplicates"
echo ""
echo "📌 لدمج عدة عمليات:"
echo "   python3 json_analyzer.py YOUR_FILE.json -a -p -d"
echo ""
echo "📌 للحصول على مساعدة كاملة:"
echo "   python3 json_analyzer.py --help"
echo ""

echo "════════════════════════════════════════════════════════════════════"
echo "  ✅ تم التشغيل بنجاح!"
echo "════════════════════════════════════════════════════════════════════"
echo ""
echo "💡 ملاحظة: يمكنك الآن استخدام الأداة على أي ملف JSON"
echo "🔗 المستودع: https://github.com/Timmyae/json-analyzer-cli"
echo ""
