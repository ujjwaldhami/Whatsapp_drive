<h1>📦 WhatsApp-Driven Google Drive Assistant</h1>

<p>A smart assistant that responds to WhatsApp messages and performs Google Drive operations like <strong>list</strong>, <strong>delete</strong>, <strong>move</strong>, and <strong>summarize</strong> using natural text commands.</p>

<h2>🚀 Features</h2>
<ul>
  <li>Twilio-powered WhatsApp webhook</li>
  <li>Command parsing and file operations</li>
  <li>Drive integration (list, delete, move)</li>
  <li>Summarization feature for Drive folders</li>
  <li>Frontend view served with Django</li>
</ul>

<h2>📂 Folder Structure</h2>
<pre>
whatsapp_drive_assistant/
├── core/
│   ├── views.py
│   └── utils/
│       └── parser.py
├── frontend/
│   └── index.html
└── manage.py
</pre>

<h2>⚙️ Setup</h2>
<ol>
  <li>Clone the repo</li>
  <li>Configure environment variables (Twilio credentials)</li>
  <li>Run Django server</li>
  <li>Expose localhost using ngrok</li>
  <li>Connect Twilio webhook to your ngrok URL</li>
</ol>

<h2>📨 Commands You Can Send</h2>
<ul>
  <li><code>LIST &lt;folder&gt;</code> – Lists files in folder</li>
  <li><code>DELETE &lt;file&gt;</code> – Deletes specified file</li>
  <li><code>MOVE &lt;file&gt; &lt;destination&gt;</code> – Moves file</li>
  <li><code>SUMMARY &lt;folder&gt;</code> – Summarizes folder content</li>
</ul>

<h2>🛠️ Tech Stack</h2>
<ul>
  <li>Django + Django REST Framework</li>
  <li>Twilio API</li>
  <li>Google Drive API</li>
</ul>

<h2>👤 Author</h2>
<p>Made with 💡 by <a href="https://github.com/ujjwaldhami">Ujjawal Dhami</a></p>
