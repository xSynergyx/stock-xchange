import React from 'react';
import { render, screen } from '@testing-library/react';
import StockTable from './StockTable.js';


test('that all stock data is displayed in an HTML table', () => {
    const testData = [
        {"Symbol": "DIS", "Company": "Walt Disney Co (The)", "High": 201.23, "Low": 175.34, "Price": 187.9, "Category": "Mega"},
        {"Symbol": "UNH", "Company": "Unitedhealth Group Inc", "High": 413.42, "Low": 391.98, "Price": 401.528, "Category": "Mega"}, 
        {"Symbol": "JPM", "Company": "JPMorgan Chase & Co.", "High": 159.21, "Low": 152.87, "Price": 156.285, "Category": "Mega"}
    ];

    render(<StockTable stocks={testData}/>);
    const stocksTable = screen.getByTestId('stocks_table');
    // Check that a table exists in the document
    expect(stocksTable).toBeInTheDocument();

    // Check that the stock data exists in the table
    for (const stock in testData) {
        expect(stocksTable).toHaveTextContent(stock);
    }
});