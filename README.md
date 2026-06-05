
# Hotel Booking Cancellation & Revenue Optimization Analysis

![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Tool](https://img.shields.io/badge/Tool-Google%20Sheets-blue)
![Domain](https://img.shields.io/badge/Domain-Hospitality%20Analytics-orange)

---

## Table of Contents

- [Project Overview](#project-overview)
- [Business Objectives](#business-objectives)
- [Dataset Description](#dataset-description)
- [Data Preparation](#data-preparation)
- [Feature Engineering](#feature-engineering)
- [Key Performance Indicators (KPIs)](#key-performance-indicators-kpis)
- [Dashboard Overview](#dashboard-overview)
- [Analytical Focus Areas](#analytical-focus-areas)
- [Key Insights](#key-insights)
- [Strategic Recommendations](#strategic-recommendations)
- [Tools & Technologies](#tools--technologies)
- [Business Impact](#business-impact)
- [Conclusion](#conclusion)

---

## Project Overview

This project analyzes hotel booking behavior to identify structural drivers of cancellations and revenue instability in the hospitality industry.

Hotels experience financial uncertainty due to:

- Fluctuating demand patterns  
- Seasonal arrival variations  
- High cancellation rates  
- Segment-specific booking behaviors  

Using **119,390 historical booking records**, this project transforms raw booking data into structured, decision-oriented business insights through KPI modeling and dashboard visualization.

---

## Business Objectives

- Identify key drivers behind booking cancellations  
- Quantify revenue loss due to cancellations  
- Analyze performance differences across hotel types  
- Understand customer segment contribution to revenue  
- Support revenue optimization and forecasting decisions  

---

## Dataset Description

- **Total Records:** 119,390  
- **Data Type:** Historical hotel booking data  
- **Key Variables:**
  - Hotel Type  
  - Arrival Year & Month  
  - Lead Time  
  - Customer Type  
  - Market Segment  
  - Deposit Type  
  - Booking Status  
  - Average Daily Rate (ADR)  
  - Revenue Metrics  

---

## Data Preparation

### Data Cleaning
- Removed duplicate records  
- Standardized categorical values  
- Treated missing values using logical imputation  
- Validated booking status consistency  

### Outlier Treatment
- Identified abnormal ADR values  
- Reviewed extreme lead time entries  
- Ensured realistic revenue calculations  

---

## Feature Engineering

To enhance analytical depth, the following features were created:

- Lead Time Buckets (0–7, 8–30, 31–90, 90+ days)  
- Revenue per Booking  
- Canceled Revenue (Lost Revenue)  
- Segment Classification Variables  
- Seasonal Arrival Indicators  

---

## Key Performance Indicators (KPIs)

The dashboard includes the following core metrics:

- Total Bookings  
- Total Revenue (INR)  
- Lost Revenue (Canceled Revenue)  
- Cancellation Rate  
- Average Daily Rate (ADR)  
- Revenue by Customer Segment  
- Revenue by Hotel Type  
- Monthly Booking Trends  

---

## Dashboard Overview

The interactive dashboard provides executive-level insights through:

### 1. Booking Trends by Year
- Growth in total bookings  
- Year-over-year revenue comparison  

### 2. Revenue by Customer Type
- Contract  
- Group  
- Transient  
- Transient-Party  

Transient customers contribute the highest share of total revenue.

### 3. Booking Status Distribution
- Confirmed  
- Canceled  
- No-Show  

This reveals overall cancellation exposure.

### 4. Hotel Type Comparison
- City Hotel vs Resort Hotel  
- Booking volume and revenue contrast  
- Cancellation differences  

### 5. ADR vs Booking Status
- Pricing sensitivity analysis  
- Identification of potential overpricing risks  

### 6. Monthly Arrival Trends
- Seasonal demand peaks  
- Low-demand identification for pricing optimization  

### 7. Revenue Loss by Hotel Type
- Financial impact of cancellations per property type  

---

## Analytical Focus Areas

### Impact of Lead Time on Cancellation Probability
Longer lead times are associated with higher cancellation likelihood, increasing forecast uncertainty.

### Deposit Policy and Revenue Stability
Non-refundable deposits reduce cancellation rates, while flexible policies increase booking volume but raise financial risk.

### Seasonal Demand Patterns
Revenue contribution varies significantly across months, indicating strong seasonality.

### Segment-Wise Revenue Contribution
Transient customers dominate revenue, while group bookings display different cancellation dynamics.

### Hotel-Type Behavioral Differences
City hotels show higher booking volumes, while resort hotels demonstrate stronger seasonal concentration.

---

## Key Insights

- Cancellation behavior is strongly linked to lead time and deposit type.  
- Revenue volatility follows identifiable seasonal and segment-based patterns.  
- Lost revenue from cancellations represents significant financial leakage.  
- Segment-based analysis enables more precise revenue management strategies.  

---

## Strategic Recommendations

- Implement dynamic pricing during peak seasons.  
- Introduce stricter deposit policies for long lead-time bookings.  
- Apply segment-specific cancellation mitigation strategies.  
- Strengthen seasonal forecasting models.  
- Monitor ADR sensitivity to reduce overpricing-related cancellations.  

---

## Tools & Technologies

- Google Sheets (Data Cleaning & Modeling)  
- Pivot Tables  
- Dashboard Visualization  
- KPI Framework Development  

---

## Business Impact

This project enables:

- Quantified revenue leakage measurement  
- Improved demand forecasting  
- Data-driven pricing strategy development  
- Enhanced revenue stability and planning  

---

## Conclusion

Hotel revenue instability is driven by structural factors including lead time, customer segmentation, deposit policy, and seasonality.

By combining structured data preprocessing, KPI development, and dashboard-based visualization, this project provides a scalable framework for cancellation risk mitigation and revenue optimization in the hospitality sector.



- <img width="1069" height="1542" alt="Screenshot 2026-02-18 at 22 53 54" src="https://github.com/user-attachments/assets/a70a7609-94a3-4fed-90c0-f3400c471b7c" />

