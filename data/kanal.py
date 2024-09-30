import sqlite3

# Assuming you already have a connection and cursor set up
conn = sqlite3.connect('channels.db')
cursor = conn.cursor()

# Create the channels table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS channels (
        channel_id TEXT PRIMARY KEY  
    )
''')
conn.commit()
#limit INTEGER DEFAULT 0
# Function to add a channel to the database
def add_channel(channel_id):
    try:
        # Check if the channel already exists in the database
        cursor.execute("SELECT * FROM channels WHERE channel_id=?", (channel_id,))
        existing_channel = cursor.fetchone()

        if not existing_channel:
            # Insert the channel into the channels table
            cursor.execute("INSERT INTO channels (channel_id) VALUES (?)", (channel_id,))
            conn.commit()
            print(f"Channel {channel_id} added to the database.")
        else:
            print(f"Channel {channel_id} already exists in the database.")
        return True    
    except Exception as e:
        print(f"Error adding channel: {e}")

# Function to remove a channel from the database
def del_channel(channel_id):
    try:
        # Check if the channel exists in the database
        cursor.execute("SELECT * FROM channels WHERE channel_id=?", (channel_id,))
        existing_channel = cursor.fetchone()

        if existing_channel:
            # Remove the channel from the channels table
            cursor.execute("DELETE FROM channels WHERE channel_id=?", (channel_id,))
            conn.commit()
            print(f"Channel {channel_id} removed from the database.")
        else:
            print(f"Channel {channel_id} not found in the database.")
        return True    
    except Exception as e:
        print(f"Error removing channel: {e}")

# Example usage
# update_channel('old_channel_id', 'new_channel_id')



def get_channels():
    try:
        # Retrieve the channels from the channels table
        cursor.execute("SELECT channel_id FROM channels")  # Corrected column name
        result = cursor.fetchall()  # Fetch all rows
        if result:
            channels_list = [row[0] for row in result]
            #print(f"Channels in the database: {', '.join(channels_list)}")
            return channels_list
        else:
            return [ ]
    except Exception as e:
        print(f"Error retrieving channels: {e}")
        return [ ]


#del_channel(new_channel_id)


