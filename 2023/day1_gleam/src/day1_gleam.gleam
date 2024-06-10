import gleam/int
import gleam/io
import gleam/list
import gleam/result
import gleam/string

pub fn main() {
  let file_content =
    get_list_of_lines(result.unwrap(read_file("./ts_t"), "No file here"))

  let list_of_line_numbers = list.map(file_content, number_in_line)
  io.debug(list.fold(list_of_line_numbers, 0, fn(a, b) { a + b }))
}

fn get_list_of_lines(file_content: String) -> List(String) {
  string.split(file_content, "\n")
}

@external(erlang, "file", "read_file")
fn read_file(path: String) -> Result(a, b)

fn number_in_line(line: String) -> Int {
  let first_dig = find_first_digit(string_to_list(line, []))
  let last_dig = find_last_digit(string_to_list(line, []))

  case int.parse(first_dig <> last_dig) {
    Ok(num) -> num
    Error(_) -> -1
  }
}

fn is_digit(input: String) -> Bool {
  let is_int = result.unwrap(int.parse(input), -1)

  is_int > -1
}

fn find_first_digit(line: List(String)) -> String {
  case line {
    [head, ..tail] ->
      case is_digit(head) {
        True -> head
        False -> find_first_digit(tail)
      }
    _ -> ""
  }
}

fn find_last_digit(line: List(String)) -> String {
  find_first_digit(list.reverse(line))
}

fn string_to_list(line: String, accumalator: List(String)) -> List(String) {
  case string.first(line) {
    Ok(char) ->
      string_to_list(
        string.drop_left(line, 1),
        list.append(accumalator, [char]),
      )
    Error(_) -> accumalator
  }
}
