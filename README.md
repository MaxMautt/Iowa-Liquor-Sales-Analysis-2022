# Iowa Liquor Sales Analysis — 2022

## Overview
SQL-based analysis of Iowa's liquor sales data sourced directly from the 
Iowa Open Data API, exploring sales performance, profitability, and 
consumption patterns across stores, vendors, cities, and product categories.

## Data Source
- **Source:** Iowa Data Portal — Open Data API
- **Records:** ~2.4 million rows
- **Year:** 2022
- **Access method:** Live API query (no static file download)

## Tools Used
- **Python** — API connection and data extraction (requests, pandas)
- **SQL (DuckDB)** — Data analysis and aggregations
- **Power BI** — Interactive dashboard and visualizations

## Analyses Performed
1. Top 10 stores by total sales and alcohol volume
2. Best-selling liquor category overall
3. Top 10 vendors by total revenue
4. Monthly sales trend throughout 2022
5. Average profit margin by liquor category
6. Top 10 cities by alcohol volume sold

## Key Findings
- **DIAGEO AMERICAS** was the top vendor with $3.2M in sales
- **American Vodkas** was the best-selling category with $2.1M in revenue
- **August** recorded the highest monthly sales at $41.3M
- **Imported Whiskies** had the highest average profit margin at $31.96/bottle
- **Des Moines** led in alcohol volume with 2.5 million liters sold

## Interactive Dashboard
[Power BI Dashboard](https://app.powerbi.com/groups/me/reports/71bcbd16-cd27-4ae4-9512-dea8b2f5ddac/2ef6d7e8d63a5f2e3b5a?experience=power-bi)

## Files
- `Analysis.py` — Data extraction and SQL analysis script
- `data/` — Exported CSV results for each analysis
