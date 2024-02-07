function getWeather() {
    const cityInput = document.getElementById('cityInput');
    const weatherInfo = document.getElementById('weatherInfo');
    const cityName = document.getElementById('cityName');
    const temperature = document.getElementById('temperature');
    const description = document.getElementById('description');
    const humidity = document.getElementById('humidity');
    const validationError = document.getElementById('validationError')

    const city = cityInput.value.trim();

    // If the user doesn't enter a city 
    if (city === '') {
        validationError.textContent = 'Please enter a city.';
        weatherInfo.classList.add('hidden');
        return;
    }

    // Clear previous validation errors
    validationError.textContent = '';


    // Make a POST request to the Flask backend
    fetch('/weather', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ city }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Failed to fetch data. Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        // Display the weather information
        cityName.textContent = `Weather in ${city}:`;
        temperature.textContent = `Temperature: ${(data.main.temp - 273.15).toFixed(2)}°C`;
        description.textContent = `Description: ${data.weather[0].description}`;
        humidity.textContent = `Humidity: ${data.main.humidity}%`;
        // Show weather information
        weatherInfo.classList.remove('hidden');
    })
    // Handle anny error comming from backend
    .catch(error => {
        console.error('Error fetching weather data:', error);
        alert('Error fetching weather data. Please try again.');
    });
}
