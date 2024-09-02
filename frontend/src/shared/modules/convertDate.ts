const options = {
  locale: 'ru-RU',
  year: 'numeric',
  month: '2-digit',
  day: '2-digit',
  hour: '2-digit',
  minute: '2-digit',
  second: '2-digit',
  hour12: false
}
export const dateFormatter = (date: Date | undefined) => {
  if (date === undefined) {
    return
  }
  return date.toLocaleString(options)
}

