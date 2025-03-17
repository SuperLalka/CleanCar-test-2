import '@testing-library/jest-dom';
import * as React from 'react';

import {render, screen} from '@testing-library/react';
import {BrowserRouter} from "react-router";

import AppNavigation from './AppNavigation';
import userEvent from "@testing-library/user-event";

test("should render <AppNavigation/>", () => {
    render(
        <BrowserRouter>
            <AppNavigation/>
        </BrowserRouter>
    );

    expect(screen.getAllByRole("link")).toHaveLength(3);

    const links = screen.getAllByRole("link");

    expect(links[0].textContent).toEqual("Home");
    expect(links[0].href).toContain("/");

    expect(links[1].textContent).toEqual("Load Image");
    expect(links[1].href).toContain("/loader");

    expect(links[2].textContent).toEqual("Gallery");
    expect(links[2].href).toContain("/gallery");
});
