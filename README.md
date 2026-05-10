# To-Do List Application

A modern, responsive to-do list application with local storage functionality built with vanilla JavaScript, HTML, and CSS.

## Features

- ✅ **Add Tasks**: Easily add new tasks to your to-do list
- ✅ **Mark Complete**: Check off tasks as you complete them
- ✅ **Delete Tasks**: Remove individual tasks from your list
- ✅ **Filter Tasks**: View all tasks, active tasks, or completed tasks
- ✅ **Local Storage**: All tasks are automatically saved to browser's local storage
- ✅ **Statistics**: View total and completed task counts
- ✅ **Clear Completed**: Remove all completed tasks at once
- ✅ **Responsive Design**: Works seamlessly on desktop and mobile devices
- ✅ **Keyboard Support**: Press Enter to add tasks quickly

## How to Use

1. **Open the Application**: Open `index.html` in your web browser
2. **Add a Task**: Type your task in the input field and click "Add Task" or press Enter
3. **Mark Complete**: Click the checkbox next to a task to mark it as complete
4. **Delete Task**: Click the "Delete" button to remove a task
5. **Filter Tasks**: Use the filter buttons (All, Active, Completed) to view different task categories
6. **Clear Completed**: Click "Clear Completed" to remove all finished tasks
7. **Data Persistence**: Your tasks are automatically saved to your browser's local storage

## File Structure

```
├── index.html      # HTML structure
├── styles.css      # Styling and responsive design
├── script.js       # JavaScript logic and local storage management
└── README.md       # This file
```

## Local Storage

The application stores all tasks in the browser's `localStorage` under the key `todos`. The data persists even after closing and reopening the browser.

### Stored Data Format

Each task is stored as an object with the following properties:
```javascript
{
    id: timestamp,
    text: "task description",
    completed: boolean,
    createdAt: "date string"
}
```

## Technical Details

- **Framework**: Vanilla JavaScript (no external dependencies)
- **Storage**: Browser's LocalStorage API
- **Responsive**: Mobile-first design with CSS media queries
- **Security**: HTML escaping to prevent XSS attacks
- **Browser Support**: Works in all modern browsers (Chrome, Firefox, Safari, Edge)

## Browser Compatibility

- Chrome/Chromium 4+
- Firefox 3.5+
- Safari 4+
- Edge (all versions)
- Opera 10.5+

## Features Explanation

### Add Tasks
Type a task in the input field and either:
- Click the "Add Task" button, or
- Press Enter on your keyboard

### Filter Options
- **All**: Shows all tasks (completed and active)
- **Active**: Shows only incomplete tasks
- **Completed**: Shows only completed tasks

### Statistics
- **Total**: Total number of tasks in your list
- **Completed**: Number of completed tasks

## Tips

- Use the filter buttons to focus on what needs to be done
- Your tasks are saved automatically - no need to manually save
- Use keyboard shortcuts (Enter) for faster task addition
- Clear your browser's data will reset all tasks

## Future Enhancements

Potential features for future versions:
- Task categories/tags
- Due dates and reminders
- Priority levels
- Task editing functionality
- Cloud synchronization
- Dark mode theme

## License

This project is open source and available for personal and commercial use.

---

Enjoy organizing your tasks with this simple yet effective to-do list application!
