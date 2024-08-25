// src/App.js
import React, { useState } from 'react';
import axios from 'axios';

const App = () => {
    const [input, setInput] = useState('');
    const [response, setResponse] = useState(null);
    const [selectedOptions, setSelectedOptions] = useState([]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const res = await axios.post('https://your-backend-url/bfhl', JSON.parse(input));
            setResponse(res.data);
        } catch (error) {
            console.error('Error making the request', error);
        }
    };

    const handleOptionChange = (e) => {
        const value = e.target.value;
        setSelectedOptions(prev => 
            prev.includes(value) ? prev.filter(option => option !== value) : [...prev, value]
        );
    };

    const renderResponse = () => {
        if (!response) return null;

        const { numbers, alphabets, highest_lowercase_alphabet } = response;
        let dataToDisplay = [];

        if (selectedOptions.includes('Numbers')) {
            dataToDisplay = [...dataToDisplay, { label: 'Numbers', data: numbers }];
        }
        if (selectedOptions.includes('Alphabets')) {
            dataToDisplay = [...dataToDisplay, { label: 'Alphabets', data: alphabets }];
        }
        if (selectedOptions.includes('Highest lowercase alphabet')) {
            dataToDisplay = [...dataToDisplay, { label: 'Highest lowercase alphabet', data: highest_lowercase_alphabet }];
        }

        return (
            <div>
                {dataToDisplay.map((item, index) => (
                    <div key={index}>
                        <h3>{item.label}</h3>
                        <pre>{JSON.stringify(item.data, null, 2)}</pre>
                    </div>
                ))}
            </div>
        );
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <textarea 
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    placeholder='Enter JSON here'
                />
                <button type='submit'>Submit</button>
            </form>
            <div>
                <label>
                    <input 
                        type='checkbox' 
                        value='Numbers' 
                        onChange={handleOptionChange}
                    /> Numbers
                </label>
                <label>
                    <input 
                        type='checkbox' 
                        value='Alphabets' 
                        onChange={handleOptionChange}
                    /> Alphabets
                </label>
                <label>
                    <input 
                        type='checkbox' 
                        value='Highest lowercase alphabet' 
                        onChange={handleOptionChange}
                    /> Highest lowercase alphabet
                </label>
            </div>
            {renderResponse()}
        </div>
    );
};

export default App;
