import gleam/dict.{type Dict}
import gleam/int
import gleam/io
import gleam/list
import gleam/string
import simplifile

pub fn main() {
  let assert Ok(file_content) = simplifile.read(from: "./input.txt")

  let file_as_list = file_content_as_list(file_content)

  let #(left, right) = loop_over_construct(file_as_list, [], [])

  let content = #(
    list.sort(left, by: int.compare),
    list.sort(right, by: int.compare),
  )

  io.debug(int.sum(distance(content, [])))
  io.debug(part_two_similarity_score(content))
}

fn file_content_as_list(file_content: String) -> List(String) {
  string.split(file_content, "\n")
}

fn loop_over_construct(
  content: List(String),
  left,
  right,
) -> #(List(Int), List(Int)) {
  case content {
    [_] -> {
      #(parse_list(left, []), parse_list(right, []))
    }
    [first, ..rest] -> {
      loop_over_construct(
        rest,
        list.append(left, [string.drop_end(first, 8)]),
        list.append(right, [string.drop_start(first, 8)]),
      )
    }
    [] -> #(parse_list(left, []), parse_list(right, []))
  }
}

fn parse_list(inn: List(String), out: List(Int)) -> List(Int) {
  case inn {
    [last] -> {
      case int.parse(last) {
        Ok(val) -> list.append(out, [val])
        Error(_) -> out
      }
    }
    [head, ..tail] -> {
      case int.parse(head) {
        Ok(val) -> parse_list(tail, list.append(out, [val]))
        Error(_) -> out
      }
    }
    [] -> out
  }
}

fn distance(inn: #(List(Int), List(Int)), out: List(Int)) -> List(Int) {
  case inn {
    #([left], [right]) -> {
      distance(#([], []), list.append(out, [int.absolute_value(left - right)]))
    }
    #([left_head, ..left_tail], [right_head, ..right_tail]) -> {
      distance(
        #(left_tail, right_tail),
        list.append(out, [int.absolute_value(left_head - right_head)]),
      )
    }
    #([], []) -> out
    #(_, _) -> out
  }
}

fn part_two_similarity_score(inn: #(List(Int), List(Int))) -> Int {
  case inn {
    #(left, right) -> {
      let right_as_dict = list_to_map(right, dict.new())

      multiply_left_to_right(left, right_as_dict, 0)
    }
  }
}

fn multiply_left_to_right(
  left: List(Int),
  right: Dict(Int, Int),
  accumalator: Int,
) -> Int {
  case left {
    [head] -> {
      case dict.get(right, head) {
        Ok(count) ->
          multiply_left_to_right([], right, accumalator + { head * count })
        Error(_) -> multiply_left_to_right([], right, accumalator)
      }
    }
    [head, ..tail] -> {
      case dict.get(right, head) {
        Ok(count) ->
          multiply_left_to_right(tail, right, accumalator + { head * count })
        Error(_) -> multiply_left_to_right(tail, right, accumalator)
      }
    }
    [] -> accumalator
  }
}

fn list_to_map(inn: List(Int), out: Dict(Int, Int)) -> Dict(Int, Int) {
  case inn {
    [head] -> {
      case dict.get(out, head) {
        Ok(count) -> {
          list_to_map([], dict.insert(out, head, count + 1))
        }
        Error(_) -> {
          list_to_map([], dict.insert(out, head, 1))
        }
      }
    }
    [head, ..tail] -> {
      case dict.get(out, head) {
        Ok(count) -> {
          list_to_map(tail, dict.insert(out, head, count + 1))
        }
        Error(_) -> {
          list_to_map(tail, dict.insert(out, head, 1))
        }
      }
    }
    [] -> out
  }
}
