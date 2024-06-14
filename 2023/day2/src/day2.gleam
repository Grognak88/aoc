import gleam/int
import gleam/io
import gleam/list
import gleam/regex.{type Match}
import gleam/result
import gleam/string

const red_max: Int = 12

const green_max: Int = 13

const blue_max: Int = 14

const pattern: String = "(\\d+) (red|green|blue)"

pub fn main() {
  let filecontent = result.unwrap(read_file("./test_data"), "No file here")

  let file_content_array = string.split(string.trim(filecontent), "\n")

  io.debug(sum_ids(file_content_array, 0))
}

@external(erlang, "file", "read_file")
fn read_file(path: String) -> Result(a, b)

fn sum_ids(games: List(String), sum: Int) -> Int {
  let assert Ok(re) = regex.from_string(pattern)

  case games {
    [] -> sum
    [head, ..rest] ->
      case matches(regex.scan(with: re, content: head)) {
        True -> {
          let assert Ok(game) =
            string.split(head, ":")
            |> list.first

          let assert Ok(string_num) =
            string.split(game, " ")
            |> list.last

          let assert Ok(num) = int.parse(string_num)
          sum_ids(rest, sum + num)
        }
        False -> {
          sum_ids(rest, sum)
        }
      }
  }
}

fn matches(list_m: List(Match)) -> Bool {
  case list_m {
    [] -> True
    [match, ..rest] -> {
      case string.split(match.content, " ") {
        [str_num, color] -> {
          let assert Ok(num) = int.parse(str_num)
          io.debug(color)
          case color {
            "blue" -> {
              case num <= blue_max {
                True -> matches(rest)
                False -> False
              }
            }
            "red" -> {
              case num <= red_max {
                True -> matches(rest)
                False -> False
              }
            }
            "green" -> {
              case num <= green_max {
                True -> matches(rest)
                False -> False
              }
            }
            _ -> matches(rest)
          }
        }
        _ -> matches(rest)
      }
    }
  }
}
