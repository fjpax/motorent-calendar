if (!window.dash_clientside) {
    window.dash_clientside = {};
}

window.dash_clientside.clientside = {
    addEvent: function(n_clicks, title, start, end, classname) {
        if (n_clicks > 0 && title && start && classname) {
            var calendarEl = document.getElementById('calendar');
            if (!window.fullCalendarInstance) {  // Check if the calendar is already initialized
                window.fullCalendarInstance = new FullCalendar.Calendar(calendarEl, {
                    initialView: 'dayGridMonth'
                });
                window.fullCalendarInstance.render();
            }

            window.fullCalendarInstance.addEvent({
                title: title,
                start: start,
                end: end || start,
                className: classname
            });
        }
        return '';  // Use an empty string to indicate no update needed
    }
};
