<h1>Dev-Watcher 🐍</h1>

<p>
Dev-Watcher is a lightweight developer utility that watches your project directory in real time and copies only added or modified files into a <code>_changes/</code> folder, preserving the original directory structure.
</p>

<p>
It is mainly useful for <strong>large projects</strong> such as <strong>Laravel</strong>, <strong>WordPress</strong>, or other PHP frameworks where many files are changed across different folders and manual FTP uploads become slow and error-prone.
</p>

<hr>

<h2>Features</h2>
<ul>
  <li>Real-time file watching (event-based)</li>
  <li>Logs added and modified files in the console</li>
  <li>Copies only changed files</li>
  <li>Preserves full directory structure</li>
  <li>Smart ignore rules (<code>.git</code>, <code>_changes</code>, <code>node_modules</code>, etc.)</li>
  <li>Supports nested vendor directories (e.g. <code>public/vendor/</code>)</li>
  <li>Cross-platform: Linux, macOS, Windows</li>
</ul>

<hr>

<h2>Requirements</h2>
<ul>
  <li>Python 3.8 or newer</li>
  <li>pip (Python package manager)</li>
</ul>

<p>Python dependency:</p>
<ul>
  <li>watchdog</li>
</ul>

<hr>

<h2>Installation</h2>

<pre>
git clone https://github.com/rytisguru/dev-watcher.git
cd devwatch
python3 -m pip install -r requirements.txt
</pre>

<p>If <code>pip</code> is missing (Ubuntu / Debian):</p>

<pre>
sudo apt install python3-pip
</pre>

<hr>

<h2>How Dev-Watcher Works</h2>
<ul>
  <li>Dev-Watcher watches the directory you run it from</li>
  <li>When a file is added or modified, it is copied to <code>_changes/</code></li>
  <li>The folder structure is preserved exactly</li>
  <li>You upload <code>_changes/</code> instead of hunting individual files</li>
</ul>

<hr>

<h2>How to Run Dev-Watcher</h2>

<p><strong>IMPORTANT:</strong><br>
Dev-Watcher watches the directory you run it from.<br>
You must open your terminal in the <strong>project root directory</strong> you want to watch.
</p>

<h3>Example: Laravel Project</h3>

<pre>
/home/user/projects/my-laravel-app/
├─ app/
├─ public/
├─ resources/
├─ routes/
└─ vendor/
</pre>

<h3>Step 1: Open terminal in project root</h3>

<h3>Step 2: Run Dev-Watcher</h3>

<pre>
python3 devwatch.py
</pre>

<p>Another example:</p>

<pre>
python3 /path/to/devwatch/devwatch.py
</pre>

<p>Dev-Watcher will immediately start watching the current directory.</p>

<h3>Step 3: Work on your project</h3>

<p>Edit and save files anywhere in the project.</p>

<pre>
Watching project...

[ADD] app/Http/Controllers/UserController.php
[COPY] → _changes/app/Http/Controllers/UserController.php

[MOD] resources/views/dashboard.blade.php
[COPY] → _changes/resources/views/dashboard.blade.php
</pre>

<h3>Step 4: Stop Dev-Watcher</h3>

<pre>
Ctrl + C
</pre>

<p>All collected files remain inside the <code>_changes/</code> directory.</p>

<hr>

<h2>Output Folder Structure</h2>

<p>If you modify:</p>

<pre>
app/Http/Controllers/UserController.php
resources/views/dashboard.blade.php
public/js/app.js
</pre>

<p>Dev-Watcher creates:</p>

<pre>
_changes/
├─ app/
│  └─ Http/
│     └─ Controllers/
│        └─ UserController.php
├─ resources/
│  └─ views/
│     └─ dashboard.blade.php
└─ public/
   └─ js/
      └─ app.js
</pre>

<p>Upload the entire <code>_changes/</code> directory contents via FTP / SFTP.</p>

<hr>

<h2>Ignore Rules</h2>

<p>Ignored by default:</p>
<ul>
  <li>.git</li>
  <li>_changes</li>
  <li>node_modules</li>
</ul>

<p>
Root-level <code>vendor/</code> directories may be ignored, while nested vendors such as:
</p>

<pre>
public/vendor/
</pre>

<p>are included.</p>

<p>Ignore logic can be adjusted inside <code>devwatch.py</code>.</p>

<hr>

<h2>Optional: Run as a Command</h2>

<p>Create a shell alias (Linux / macOS):</p>

<pre>
alias devwatch="python3 /full/path/to/devwatch.py"
</pre>

<p>Then run from any project root:</p>

<pre>
devwatch
</pre>

<hr>

<h2>Notes</h2>
<ul>
  <li>Files in <code>_changes/</code> are overwritten on each modification</li>
  <li>Deleted files are not tracked</li>
  <li>Designed for large projects with many nested folders</li>
  <li>Ideal for FTP / SFTP deployment workflows</li>
</ul>

<hr>

<h2>License</h2>
<p>MIT License © 2026 Rytis Plečkauskas</p>
