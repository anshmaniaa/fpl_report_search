import csv
import os

# Define the reports and their URLs
reports = [
    {
        "description": "An exhaustive analysis reviewing power consumption metrics across all units and facilities. This report benchmarks against previous months and years, highlighting any significant power surges or drops, and offers insights for potential optimization to reduce wastage and costs.",
        "link": "http://floridapowerlimited/reports/monthlyconsumption"
    },
    {
        "description": "A comprehensive yearly review that dives deep into the environmental footprint of operations. It showcases quantified emissions data, sustainability initiatives undertaken, waste management protocols, and any regulatory compliance updates to ensure environmentally conscious operations.",
        "link": "http://floridapowerlimited/reports/environmentalimpact"
    },
    {
        "description": "A meticulously prepared documentation detailing scheduled maintenance activities, equipment health checks, and planned upgrades. It assists in tracking the life cycle of power generation and distribution equipment and ensures proactive fault prevention.",
        "link": "http://floridapowerlimited/reports/maintenanceandschedules"
    },
    {
        "description": "A quarterly financial breakdown that covers revenues, operational expenses, capital expenditures, profit margins, and a comparative analysis with past quarters. Insights include economic forecasts and financial health indicators.",
        "link": "http://floridapowerlimited/reports/quarterlyfinancials"
    },
    {
        "description": "A systematic compilation that captures the voice of the customer, cataloging feedback, complaints, praises, and resolutions. It offers analytics on recurring issues, response times, and areas of improvement, serving as a feedback loop for service enhancement.",
        "link": "http://floridapowerlimited/reports/customerfeedback"
    },
    {
        "description": "A comprehensive study of the power grid's robustness, showcasing stability metrics, outage instances, their durations, root causes, and subsequent remediation actions. It aids in ensuring consistent power delivery and minimizes disruptions.",
        "link": "http://floridapowerlimited/reports/gridstability"
    },
    {
        "description": "A progress report detailing efforts to bolster the incorporation of renewable energy sources. It chronicles the challenges faced, technological adaptations, milestones achieved, and the future roadmap for a green power grid.",
        "link": "http://floridapowerlimited/reports/renewableintegration"
    },
    {
        "description": "A thorough analysis of workforce efficiency, capturing productivity metrics, and emphasizing the training programs rolled out. It discusses the skills enhancement initiatives, safety protocols, and key takeaways to ensure a skilled and safe workforce.",
        "link": "http://floridapowerlimited/reports/workforceproductivity"
    },
    {
        "description": "A strategic overview of supply chain relationships, evaluating supplier performance, contract compliance, and partnership benefits. It assists in ensuring timely delivery, cost-effectiveness, and strong partnerships for sustained operations.",
        "link": "http://floridapowerlimited/reports/supplierrelations"
    },
    {
        "description": "A forward-looking document that provides insights into energy market dynamics. It covers a competitor analysis, potential growth areas, emerging market trends, and possible challenges, setting a strategic direction for the future.",
        "link": "http://floridapowerlimited/reports/marketanalysis"
    }
]

# Path to the output CSV file
csv_file_path = 'reports.csv'

# Writing to csv
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(["Description", "Link"])
    # Write the data
    for report in reports:
        writer.writerow([report["description"], report["link"]])

# Confirm the file is created
os.path.exists(csv_file_path)
