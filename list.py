from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def create_budget_pdf():
    pdf_file = "Smart_Glasses_Budget.pdf"
    doc = SimpleDocTemplate(pdf_file, pagesize=A4)
    elements = []
    styles = getSampleStyleSheet()
    
    # Custom Styles
    title_style = styles['Heading1']
    title_style.alignment = 1  # Center
    
    # Header Information
    elements.append(Paragraph("Project Budget: Smart Assistive Glasses", title_style))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph("Prepared for: Final Year Project Development", styles['Normal']))
    elements.append(Spacer(1, 24))

    # Budget Data
    data = [
        ['Category', 'Component', 'Detail', 'Approx. Cost (₹)'],
        ['Computing', 'Raspberry Pi 5', '8GB RAM Latest Gen', '8,500 – 9,500'],
        ['Computing', 'Active Cooler', 'Official Pi 5 Cooler', '500'],
        ['Storage', 'MicroSD Card', '64GB UHS-I SanDisk', '1,000'],
        ['Vision', 'Pi Camera Module 3', '12MP Autofocus', '3,500 – 4,000'],
        ['Sensing', 'Ultrasonic Sensor', 'JSN-SR04T Waterproof', '600'],
        ['Sensing', 'IMU (9-DOF)', 'MPU9250 / BNO055', '900 – 1,500'],
        ['Audio', 'Headset', 'Bone Conduction type', '3,000 – 4,500'],
        ['UI', 'Push Button', 'Industrial Tactile', '100'],
        ['Power', 'Power Bank', '20,000 mAh PD Support', '2,000 – 2,500'],
        ['Power', 'USB-C Cable', 'High Current PD', '300'],
        ['Build', 'Enclosure', 'Custom / 3D Printed', '1,000 – 1,500'],
        ['Build', 'Misc', 'Wiring & Mounts', '500'],
        ['', '', 'TOTAL ESTIMATED COST', '₹21,900 – ₹27,000']
    ]

    # Create Table
    budget_table = Table(data, colWidths=[80, 130, 150, 100])
    
    # Table Styling
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#2E5077")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('BACKGROUND', (0, 1), (-1, -2), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor("#F2F2F2")),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
    ])
    
    budget_table.setStyle(style)
    elements.append(budget_table)
    
    # Footer Note
    elements.append(Spacer(1, 30))
    elements.append(Paragraph("* Note: Costs are based on current market rates in India and are subject to change.", styles['Italic']))

    # Build PDF
    doc.build(elements)
    print(f"Successfully generated: {pdf_file}")

if __name__ == "__main__":
    create_budget_pdf()