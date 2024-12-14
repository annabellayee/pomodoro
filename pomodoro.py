# START application
#     IMPORT required libraries
#     SET work_duration = 25 minutes
#     SET short_break_duration = 5 minutes
#     SET long_break_duration = 15 minutes
#     SET work_cycles = 4

#     FUNCTION start_timer():
#         FOR each cycle in work_cycles:
#             CALL countdown(work_duration, "Work cycle X")
#             CALL countdown(short_break_duration, "Short Break")
#         END FOR
#         CALL countdown(long_break_duration, "Long Break")
#         DISPLAY "Pomodoro session complete!"

#     FUNCTION countdown(seconds, message):
#         WHILE seconds > 0:
#             CALCULATE minutes, seconds
#             UPDATE timer label with message and remaining time
#             REFRESH GUI
#             WAIT 1 second
#             DECREMENT seconds by 1
#         END WHILE

#     SETUP GUI layout:
#         CREATE main window
#         ADD timer label
#         ADD start button (linked to start_timer)

#     START GUI event loop
# END application
