<h1 align="center">Analytics Dashboard Prototype</h1>

<p align="center">
  A lightweight analytics dashboard built to demonstrate how marketing and sales data
  from different platforms can be pulled, combined, transformed, and visualized
  in a simple interactive interface.
</p>

<hr>

<h2>Project Description</h2>

<p>
  This project implements a <strong>simple analytics dashboard prototype</strong> designed to
  simulate a real-world business reporting workflow. The goal of the project is to show how
  data from external platforms such as <strong>Meta Ads (Facebook Ads)</strong> and
  <strong>SamCart</strong> can be integrated into a single reporting layer, transformed into
  meaningful business metrics, and displayed through an interactive user interface.
</p>

<p>
  The dashboard focuses on the core analytics pipeline:
</p>

<ul>
  <li>Programmatically retrieving data from source systems</li>
  <li>Combining and transforming that data into a unified structure</li>
  <li>Calculating useful business and performance metrics</li>
  <li>Presenting results in a simple dashboard for quick analysis</li>
</ul>

<p>
  The project is intentionally lightweight and prototype-oriented. It prioritizes
  <strong>clarity of implementation, modularity, and speed of development</strong> rather than
  production-level complexity. This makes it suitable for demonstrating engineering approach,
  API integration design, and dashboard thinking within a short development window.
</p>

<hr>

<h2>Why I Chose Gradio UI</h2>

<p>
  For this project, I chose <strong>Gradio</strong> as the UI framework because it is one of the
  fastest and cleanest ways to build an interactive Python-based web interface for a prototype.
</p>

<p>
  My preference for using Gradio was based on the following considerations:
</p>

<ul>
  <li><strong>Fast prototyping:</strong> Gradio allows rapid development of interactive interfaces without requiring separate frontend engineering.</li>
  <li><strong>Python-native workflow:</strong> Since the data retrieval, transformation, and metric calculations are already implemented in Python, Gradio integrates naturally into the same stack.</li>
  <li><strong>Minimal overhead:</strong> The assignment focuses more on API usage, data transformation, and practical solution design than on building a full frontend application.</li>
  <li><strong>Built-in UI components:</strong> Gradio provides ready-to-use components for inputs, tables, buttons, and plots, which makes it well suited for analytics dashboards.</li>
  <li><strong>Clean presentation:</strong> It offers a simple but effective way to present business metrics and trends in a structured, user-friendly layout.</li>
</ul>

<p>
  In short, Gradio was selected because it enables a <strong>practical, efficient, and readable implementation</strong>
  while keeping the project focused on the data workflow itself.
</p>

<hr>

<h2>Method Used</h2>

<p>
  The implementation follows a straightforward analytics pipeline that mirrors how many real reporting
  systems work at a simplified level.
</p>

<h3>1. Data Retrieval</h3>

<p>
  The application is structured to pull data from two separate platform sources:
</p>

<ul>
  <li><strong>Meta Ads:</strong> marketing-related metrics such as ad spend, clicks, and impressions</li>
  <li><strong>SamCart:</strong> sales-related metrics such as purchases and revenue</li>
</ul>

<p>
  For this prototype, the project uses <strong>mock API-style data</strong> to simulate the responses from these platforms.
  This keeps the solution fast to build while still reflecting the correct integration structure.
  The code is organized so that mock adapters can later be replaced by real authenticated API calls
  without changing the rest of the dashboard logic.
</p>

<h3>2. Data Transformation</h3>

<p>
  After retrieval, the raw source data is converted into structured tabular format using
  <strong>pandas DataFrames</strong>. The transformation stage includes:
</p>

<ul>
  <li>Normalizing source data into a consistent schema</li>
  <li>Merging marketing and sales datasets using the <strong>date</strong> field</li>
  <li>Handling missing values</li>
  <li>Preparing the final combined dataset for metric computation and display</li>
</ul>

<h3>3. Metric Calculation</h3>

<p>
  Once the data is combined, the system computes key performance indicators that are commonly used
  in marketing and e-commerce reporting.
</p>

<p><strong>The main metrics calculated are:</strong></p>

<ul>
  <li><strong>Total Spend</strong> – total advertising cost across the selected period</li>
  <li><strong>Total Revenue</strong> – total revenue generated from purchases</li>
  <li><strong>ROAS (Return on Ad Spend)</strong> – revenue divided by ad spend</li>
  <li><strong>Total Purchases</strong> – total number of conversions</li>
  <li><strong>CPA (Cost Per Acquisition)</strong> – spend divided by purchases</li>
  <li><strong>Conversion Rate</strong> – purchases divided by clicks</li>
</ul>

<h3>4. Visualization</h3>

<p>
  The processed data is then displayed in an interactive dashboard using Gradio. The dashboard provides:
</p>

<ul>
  <li>A summary metrics table</li>
  <li>A combined daily dataset view</li>
  <li>A trend chart comparing spend and revenue over time</li>
</ul>

<hr>

<h2>Inputs</h2>

<p>
  The dashboard accepts a small set of user inputs to keep the experience simple and focused.
</p>

<table>
  <tr>
    <th align="left">Input</th>
    <th align="left">Description</th>
  </tr>
  <tr>
    <td>Start Date</td>
    <td>The beginning date for the analytics range</td>
  </tr>
  <tr>
    <td>End Date</td>
    <td>The ending date for the analytics range</td>
  </tr>
  <tr>
    <td>Load Dashboard Button</td>
    <td>Triggers data retrieval, transformation, metric calculation, and visualization</td>
  </tr>
</table>

<p>
  These inputs allow the user to request performance data for a selected time window and refresh the dashboard accordingly.
</p>

<hr>

<h2>Outputs</h2>

<p>
  The system generates three main output sections.
</p>

<h3>1. KPI Metrics Table</h3>

<p>
  This section displays the aggregated business metrics calculated from the combined dataset.
  It provides a quick summary of the overall performance for the selected date range.
</p>

<ul>
  <li>Total Spend</li>
  <li>Total Revenue</li>
  <li>ROAS</li>
  <li>Purchases</li>
  <li>CPA</li>
  <li>Conversion Rate</li>
</ul>

<h3>2. Combined Daily Data Table</h3>

<p>
  This section displays the merged daily dataset that combines marketing and sales data into a single table.
  It makes the underlying records transparent and easy to inspect.
</p>

<p><strong>Typical columns include:</strong></p>

<ul>
  <li>Date</li>
  <li>Spend</li>
  <li>Clicks</li>
  <li>Impressions</li>
  <li>Purchases</li>
  <li>Revenue</li>
</ul>

<h3>3. Trend Chart</h3>

<p>
  The dashboard also includes a visual trend chart that compares <strong>advertising spend</strong> and
  <strong>revenue</strong> over time. This makes it easier to quickly identify performance patterns,
  relative efficiency, and the relationship between acquisition cost and generated revenue.
</p>

<hr>

<h2>About the UI</h2>

<p>
  The user interface is built using <strong>Gradio Blocks</strong>, which allows the application to be structured
  into clear sections while maintaining a simple and functional layout.
</p>

<p><strong>The UI is organized into the following parts:</strong></p>

<h3>Input Section</h3>
<ul>
  <li>Start Date field</li>
  <li>End Date field</li>
  <li>Load Dashboard button</li>
</ul>

<h3>Metrics Section</h3>
<ul>
  <li>Tabular KPI display for high-level performance review</li>
</ul>

<h3>Data Section</h3>
<ul>
  <li>Merged dataset table for detailed inspection of transformed records</li>
</ul>

<h3>Visualization Section</h3>
<ul>
  <li>Trend chart showing spend and revenue by date</li>
</ul>

<p>
  The UI is intentionally minimal and readable. The purpose is not to build a heavily styled frontend,
  but to present the analytics workflow clearly and effectively. This design keeps the emphasis on:
</p>

<ul>
  <li>Data integration</li>
  <li>Metric computation</li>
  <li>Clarity of results</li>
  <li>Ease of use</li>
</ul>

<hr>

<h2>Implementation Details</h2>

<p>
  The project is implemented in a modular structure so that each layer of the workflow remains clean and easy to maintain.
</p>

<pre><code>analytics-dashboard/
│
├── app.py
├── data_sources.py
├── transform.py
├── requirements.txt
└── README.md
</code></pre>

<h3><code>data_sources.py</code></h3>

<p>
  This module is responsible for retrieving source data. It contains adapter-style functions for:
</p>

<ul>
  <li>Meta Ads data retrieval</li>
  <li>SamCart data retrieval</li>
</ul>

<p>
  In the current prototype, these functions generate mock data that simulates real API responses.
  The structure is intentionally designed to mirror actual platform integration logic, making it easy
  to replace the mock implementations with real API calls later.
</p>

<h3><code>transform.py</code></h3>

<p>
  This module handles all processing and business logic. Its responsibilities include:
</p>

<ul>
  <li>Converting raw source data into DataFrames</li>
  <li>Merging source datasets</li>
  <li>Cleaning and filling missing values</li>
  <li>Calculating business metrics</li>
  <li>Producing a final dataset ready for presentation</li>
</ul>

<h3><code>app.py</code></h3>

<p>
  This is the main application entry point and contains the Gradio UI. It coordinates the full workflow:
</p>

<ol>
  <li>Receives user-selected input dates</li>
  <li>Calls data source functions</li>
  <li>Passes raw data into the transformation layer</li>
  <li>Calculates metrics and chart-ready outputs</li>
  <li>Displays all results in the dashboard</li>
</ol>

<p>
  This separation makes the application easier to understand, test, and extend.
</p>

<hr>

<h2>Tech Stack</h2>

<ul>
  <li><strong>Python</strong> – core programming language</li>
  <li><strong>Gradio</strong> – interactive dashboard UI</li>
  <li><strong>pandas</strong> – data manipulation and transformation</li>
  <li><strong>Plotly</strong> – chart generation</li>
  <li><strong>requests</strong> – API integration layer structure</li>
</ul>

<hr>

<h2>How to Run the Project</h2>

<p><strong>1. Install dependencies</strong></p>

<pre><code>pip install -r requirements.txt
</code></pre>

<p><strong>2. Run the application</strong></p>

<pre><code>python app.py
</code></pre>

<p>
  After execution, the Gradio app will launch locally in the browser, where the dashboard can be used interactively.
</p>

<hr>

<h2>Design Considerations</h2>

<p>
  This project was designed with the following priorities:
</p>

<ul>
  <li><strong>Rapid development:</strong> complete the prototype quickly without unnecessary complexity</li>
  <li><strong>Clear architecture:</strong> keep data retrieval, transformation, and UI separate</li>
  <li><strong>Business relevance:</strong> compute metrics that are actually useful in performance analysis</li>
  <li><strong>Extensibility:</strong> keep the structure ready for real API integration later</li>
</ul>

<hr>

<h2>Future Improvements</h2>

<p>
  The prototype can be extended further in several ways:
</p>

<ul>
  <li>Replace mock data with real Meta Ads and SamCart API integrations</li>
  <li>Add API authentication and secure credential handling</li>
  <li>Support additional marketing or e-commerce platforms</li>
  <li>Include filters for campaign, product, or platform-level analysis</li>
  <li>Add downloadable reports and CSV export</li>
  <li>Store historical data in a database for persistent analytics</li>
  <li>Expand the dashboard with more advanced business insights and visualizations</li>
</ul>

<hr>

<h2>Conclusion</h2>

<p>
  This project demonstrates a practical approach to building a <strong>simple analytics dashboard prototype</strong>
  that pulls data from multiple platform sources, combines and transforms it into a unified analytical view,
  computes meaningful performance metrics, and presents results through an interactive Gradio interface.
</p>

<p>
  Choosing <strong>Gradio</strong> made it possible to focus on the most important parts of the assignment:
  data integration, transformation logic, metric calculation, and clean presentation of results.
  The final implementation is lightweight, modular, and suitable as a fast prototype that can later be expanded
  into a more production-ready analytics solution.
</p>
