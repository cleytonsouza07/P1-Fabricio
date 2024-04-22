const userRepository = require('../repositories/userRepository');

class UserController {
  async registerUser(req, res) {
    try {
      const { username, password } = req.body;
      const existingUser = await userRepository.findUserByUsername(username);
      
      if (existingUser) {
        return res.status(400).json({ error: 'Usuário já existe' });
      }

      const newUser = await userRepository.createUser({ username, password });
      res.status(201).json(newUser);
    } catch (error) {
      res.status(500).json({ error: error.message });
    }
  }
}

module.exports = new UserController();
