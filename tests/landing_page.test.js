import { render, screen } from '@testing-library/react';
import App from './App';

test('Stock XChange logo and Login button in displayed', () => {
  render(<App />);
  
  const joinElement = screen.getByText('Stock XChange');
  expect(joinElement).toBeInTheDocument();
  
  const joinButtonElement = screen.getByText('Login');
  expect(joinButtonElement).toBeInTheDocument();
  
  //fireEvent.click(joinButtonElement); (must import)
});