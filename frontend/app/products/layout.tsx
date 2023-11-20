import React from 'react';

export default function ProductsLayout({ children }: { children: React.ReactNode}) {
    return (
        <div className="flex flex-col items-center justify-center min-h-screen py-2">
            {children}
        </div>
    );
}

