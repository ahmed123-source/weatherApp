// static/js/main.js
function getWeather() {
    const cityInput = document.getElementById('cityInput');
    const weatherInfo = document.getElementById('weatherInfo');

    const city = cityInput.value.trim();

    if (city === '') {
        alert('Please enter a city.');
        return;
    }

    // Make a POST request to the Flask backend
    fetch('/weather', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ city }),
    })
    .then(response => response.json())
    .then(data => {
        // Display the weather information
        weatherInfo.innerHTML = `Weather in ${city}: ${(data.main.temp - 273.15).toFixed(2)}°C, ${data.weather[0].description}`;
    })
    .catch(error => {
        console.error('Error fetching weather data:', error);
        alert('Error fetching weather data. Please try again.');
    });
}
