class Day6:

    def start_marker(self, buffer, option):
        start = 0
        end = option
        buffer_len = len(buffer)

        while True:
            marker = buffer[start:end]
            common = filter(lambda x: marker.count(x) >= 2, marker)

            if len(set(common)) == 0:
                print('Different at character',end,'with',buffer[start:end])
                return end

            start += 1
            end += 1

            if end == buffer_len:
                break

        return -1
