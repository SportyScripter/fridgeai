import React from 'react';
import { ListOfProductsProps } from '@/app/index';

export default function ListOfProducts({ items }: ListOfProductsProps) {
  return (
    <table>
      <thead>
        <tr>
          <th style={tableHeaderThin}>ID</th>
          <th style={tableHeaderThick}>Nazwa</th>
          <th style={tableHeaderThin}>Ilość</th>
          <th style={tableHeaderThin}>Gramatura</th>
        </tr>
      </thead>
      <tbody>
        {items.map((item, key) => (
          <tr key={key}>
            <td style={tableCellStyle}>{item.id}</td>
            <td style={tableCellStyle}>{item.name}</td>
            <td style={tableCellStyle}>{item.quantity}</td>
            <td style={tableCellStyle}>{item.unit}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

const tableHeaderThin = {
  backgroundColor: '#4f4f4f',
  padding: '10px',
  border: '2px solid #ddd',
  width: '50px',
};

const tableHeaderThick = {
  backgroundColor: '#4f4f4f',
  padding: '10px',
  border: '2px solid #ddd',
  width: '50%',
};

const tableCellStyle = {
  padding: '10px',
  border: '1px solid #ddd',
};
