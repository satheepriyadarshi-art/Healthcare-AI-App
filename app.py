<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HealthPredict AI Dashboard</title>
    <style>
        :root { --primary: #2c3e50; --secondary: #3498db; --danger: #e74c3c; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f4f7f6; color: var(--primary); padding: 20px; }
        .container { max-width: 800px; margin: auto; background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
        h1 { text-align: center; color: var(--primary); border-bottom: 2px solid #eee; padding-bottom: 10px; }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; font-weight: bold; }
        select, input { width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 6px; box-sizing: border-box; }
        button { width: 100%; padding: 12px; background: var(--secondary); color: white; border: none; border-radius: 6px; cursor: pointer; font-size: 16px; margin-top: 10px; }
        button:hover { background: #2980b9; }
        #results { margin-top: 25px; display: none; padding: 20px; border-radius: 8px; background: #ebf5fb; }
        .risk-high { color: var(--danger); font-weight: bold; }
        .metric-box { display: flex; justify-content: space-between; margin-bottom: 10px; border-bottom: 1px dashed #ccc; padding-bottom: 5px; }
    </style>
</head>
<body>

<div class="container">
    <h1>🏥 HealthPredict AI</h1>
    <p style="text-align: center;">Predictive Admission Analysis for Hospital Operations</p>
    
    <div class="form-group">
        <label>Patient Age</label>
        <input type="number" id="age" placeholder="e.g. 45" value="45">
    </div>

    <div class="form-group">
        <label>Medical Condition</label>
        <select id="condition">
            <option value="Cancer">Cancer</option>
            <option value="Diabetes">Diabetes</option>
            <option value="Asthma">Asthma</option>
            <option value="Obesity">Obesity</option>
            <option value="Hypertension">Hypertension</option>
        </select>
    </div>

    <div class="form-group">
        <label>Admission Type</label>
        <select id="admission">
            <option value="Emergency">Emergency</option>
            <option value="Urgent">Urgent</option>
            <option value="Elective">Elective</option>
        </select>
    </div>

    <button onclick="runAI()">Analyze Patient Data</button>

    <div id="results">
        <h3>Analysis Results</h3>
        <div class="metric-box">
            <span>Estimated Billing:</span>
            <span id="bill-result" style="font-weight: bold;"></span>
        </div>
        <div class="metric-box">
            <span>Clinical Risk Level:</span>
            <span id="risk-result"></span>
        </div>
        <div class="metric-box">
            <span>Recommended Action:</span>
            <span id="action-result"></span>
        </div>
    </div>
</div>

<script>
    function runAI() {
        // 1. Get Inputs
        const age = document.getElementById('age').value;
        const condition = document.getElementById('condition').value;
        const admission = document.getElementById('admission').value;

        // 2. Mock Logic based on Dataset Trends
        // Average billing in your dataset is ~$25,000
        let baseBill = 25000;
        if (condition === 'Cancer') baseBill += 5000;
        if (admission === 'Emergency') baseBill += 3000;
        if (age > 60) baseBill += 2000;

        // Risk Assessment
        let risk = "Low";
        let action = "Standard Ward Assignment";
        
        if (age > 70 || (condition === 'Cancer' && admission === 'Emergency')) {
            risk = "High";
            action = "Immediate Specialist Consultation";
        } else if (age > 50 || admission === 'Urgent') {
            risk = "Moderate";
            action = "Enhanced Monitoring";
        }

        // 3. Display Results
        document.getElementById('results').style.display = 'block';
        document.getElementById('bill-result').innerText = "$" + baseBill.toLocaleString();
        
        const riskSpan = document.getElementById('risk-result');
        riskSpan.innerText = risk;
        riskSpan.className = risk === "High" ? "risk-high" : "";
        
        document.getElementById('action-result').innerText = action;
    }
</script>

</body>
</html>
