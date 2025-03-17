import * as React from 'react';

import '@testing-library/jest-dom';
import userEvent from '@testing-library/user-event';
import {render, screen} from '@testing-library/react';

import App from './App';

test("should render <App/>", () => {
  render(<App/>);

  expect(screen.getByText(/Home/i)).toBeInTheDocument();
  userEvent.click(screen.getByText(/Home/i));
  expect(screen.getByText(/Home/i)).toBeInTheDocument();

  // expect(screen.getByText(/Load Image/i)).toBeInTheDocument();
  // userEvent.click(screen.getByText(/Load Image/i));
  // expect(screen.getByText(/Загрузчик/i)).toBeInTheDocument();

  expect(screen.getByText(/Gallery/i)).toBeInTheDocument();
  userEvent.click(screen.getByText(/Gallery/i));
  expect(screen.getByText(/Галерея/i)).toBeInTheDocument();
});
